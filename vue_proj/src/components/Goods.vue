<script setup name="GoodsView" lang="ts">
  import {Ref, ref} from "vue";
  import apis from "../api/index.js";
  import {useRoute, useRouter} from "vue-router";
  import {MODE_GOODS} from "../config";
  import {formatNowDateTime} from "../utils/TimeUtil";
  import {objectIsNull} from "../utils/ObjectUtils";
  import {ElMessageBox, ElNotification} from "element-plus";
  import {Delete, Edit} from "@element-plus/icons-vue";
  import {stringIsEmpty} from "../utils/StringUtils";
  import api from "../api";
  import Cookies from "js-cookie";

  interface Goods {
    mode?: string
    name: string
    comment?: string
    status?: string
    updated_time: string
    created_time: string
    is_deleted?: string
    box_name?: string
  }

  let goodsData: Ref<Goods[]> = ref([])
  let deletedGoods: Ref<Goods[]> = ref([])

  let boxName: string

  const $router = useRouter()
  const route = useRoute()
  if (Object.keys(route.query).length === 0){
    boxName = Cookies.get('boxName')
    if (stringIsEmpty(boxName)){
      api.openBox().then(res =>{
        $router.push({
          path: '/',
          query: { boxName: res.data }
        })
        Cookies.set('boxName', res.data)
      })
    } else {
      $router.push({
        path: '/',
        query: { boxName: boxName }
      })
    }
  } else {
    boxName = route.query.boxName.toString()
  }

  apis.getAllGoods(boxName).then(res =>{
    goodsData.value = res.data.data
    deletedGoods.value = goodsData.value
        .filter(goods => goods.is_deleted === true)
    goodsData.value = goodsData.value
        .filter(goods => goods.is_deleted !== true)
  })

  defineProps({
    key: Number
  })

  const emit = defineEmits(['refresh-goods'])

  const delGoods = (goodsName) => {
    apis.deleteItem(MODE_GOODS, goodsName).then(res =>{
      emit('refresh-goods')
    })
  }

  const permanentlyDelGoods = (goodsName) => {
    apis.permanentlyDelete(MODE_GOODS, goodsName).then(res =>{
      ElNotification({
        title: "Success",
        message: "Delete goods successfully!",
        showClose: false
      })
      emit('refresh-goods')
    })
  }

  const restore = (goodsName) => {
    apis.restoreItem(MODE_GOODS, goodsName).then(res =>{
      emit('refresh-goods')
    })
  }

  let newGoods: Ref<Goods> = ref({
    mode: MODE_GOODS,
    name: null,
    comment: null,
    status: 'full',
    updated_time: null,
    created_time: null,
    box_name: boxName
  })
  let isAddGoodsDialog: Ref<boolean> = ref(false)

  const handleAddDialogClose = (done: () => void) => {
    if (objectIsNull(newGoods.value,
        ['mode', 'status', 'updated_time', 'created_time', 'box_name'])) {
      done()
    } else {
      ElMessageBox.confirm(
        'Changes not saved, are you sure you want to close it?',
        'Warning',
        {
          confirmButtonText: 'Back',
          cancelButtonText: 'Close',
        })
        .then(() => {})
        .catch(() => { done() }
      )
    }
  }

  const onSubmitAddGoodsForm = () => {
    newGoods.value.updated_time = newGoods.value.created_time = formatNowDateTime()
    apis.addGoods(newGoods).then(res =>{
      isAddGoodsDialog = ref(false)
      ElNotification({
        title: "Success",
        message: "Add goods successfully!",
        showClose: false
      })
      emit('refresh-goods')
    })
  }

  let isEditGoodsDialog: Ref<boolean> = ref(false)
  let editingGoods: Ref<Goods>
  let beforeEditGoods: Goods

  const openEditGoodsDialog = (goods: Goods) => {
    isEditGoodsDialog.value = true
    beforeEditGoods = goods
    editingGoods = ref(Object.assign({}, goods))
  }

  const handleEditFormInput = (col: string, value: string) => {
    if (beforeEditGoods !== editingGoods.value) {
      editingGoods.value.updated_time = formatNowDateTime()
      apis.updateGoods(editingGoods.value.box_name, editingGoods.value.name, col, value, editingGoods.value.updated_time).then(res =>{
        console.log(res)
      })
    }
  }
</script>

<template>
  <!--  Add Goods-->
  <el-button @click="isAddGoodsDialog = true">Add Goods</el-button>

  <el-dialog
    v-model="isAddGoodsDialog" :before-close="handleAddDialogClose"
    title="Add New Goods" width="60%" align-center draggable>
    <el-form id="addBoxForm" :model="newGoods">
      <el-form-item label="Name">
        <el-input v-model="newGoods.name" />
      </el-form-item>
      <el-form-item label="Status">
        <el-input v-model="newGoods.status" />
      </el-form-item>
      <el-form-item label="Comment">
        <el-input v-model="newGoods.comment" type="textarea" autosize />
      </el-form-item>
    </el-form>
    <template #footer>
      <span>
        <el-button type="primary" @click="onSubmitAddGoodsForm">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>

<!--  Goods Gallery-->
  <el-descriptions :title='`${goods.name} ${goods.status}`' v-for="goods in goodsData" :column=2 border>
      <template #extra>
        <el-button  @click="delGoods(goods.name)"
                    type="danger" :icon="Delete" circle />
        <el-button @click="openEditGoodsDialog(goods)"
                   type="primary" :icon="Edit" circle />
      </template>
        <el-descriptions-item label="Updated time">{{goods.updated_time}}</el-descriptions-item>
        <el-descriptions-item label="Created time">{{goods.created_time}}</el-descriptions-item>
        <el-descriptions-item label="Comment">{{goods.comment}}</el-descriptions-item>
      </el-descriptions>

<!--  <el-table :data="goodsData" style="width: 100%">-->
<!--    <el-table-column prop="name" label="Name" width="180" />-->
<!--    <el-table-column prop="status" label="Status" width="70" />-->
<!--    <el-table-column prop="updated_time" label="Updated time" width="130" />-->
<!--    <el-table-column prop="created_time" label="Created time" width="130" />-->
<!--    <el-table-column prop="comment" label="Comment" width="200" />-->
<!--    <el-table-column fixed="right" label="Operations" width="120">-->
<!--      <template #default="scope">-->
<!--        <el-button link type="primary" size="small" @click="delGoods(scope.row.name)">-->
<!--          Delete-->
<!--        </el-button>-->
<!--      </template>-->
<!--    </el-table-column>-->
<!--  </el-table>-->

<!--  Edit Goods-->
  <el-dialog
    v-model="isEditGoodsDialog"
    title="Edit Goods" width="60%" align-center draggable>
    <el-form :model="editingGoods">
      <el-form-item label="Name">
        <el-input v-model="editingGoods.name" @input="handleEditFormInput('name', editingGoods.name)" />
      </el-form-item>
      <el-form-item label="Status">
        <el-input v-model="editingGoods.status" @input="handleEditFormInput('status', editingGoods.status)" />
      </el-form-item>
      <el-form-item label="Comment">
        <el-input v-model="editingGoods.comment" @input="handleEditFormInput('comment', editingGoods.comment)"
                  type="textarea" autosize />
      </el-form-item>
    </el-form>
    <template #footer>
      <span>
        <el-button type="primary" @click="onSubmitAddGoodsForm">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>

<!--  Trash bin-->
  <el-collapse accordion>
    <el-collapse-item title="Trash">
      <el-collapse>
        <el-collapse-item v-for="goods in deletedGoods">
          <template #title>
            <el-col :span="18">
              <div style="text-align: left">  {{goods.name}}</div>
            </el-col>
            <el-col :span="6"><div>
                <el-popconfirm width="240" title="Are you sure to delete this?">
                  <template #reference>
                    <el-button type="danger" @click="permanentlyDelGoods(goods.name)">Delete</el-button>
                  </template>
                </el-popconfirm>
                <el-button @click="restore(goods.name)">Restore</el-button>
            </div></el-col>
          </template>

          <el-descriptions>
            <el-descriptions-item label="Status">{{goods.status}}</el-descriptions-item>
            <el-descriptions-item label="Updated time">{{goods.updated_time}}</el-descriptions-item>
            <el-descriptions-item label="Created time">{{goods.created_time}}</el-descriptions-item>
            <el-descriptions-item label="Comment">{{goods.comment}}</el-descriptions-item>
          </el-descriptions>
        </el-collapse-item>
      </el-collapse>
    </el-collapse-item>
  </el-collapse>

</template>

<style scoped>

</style>