<script setup name="GoodsView" lang="ts">
import {computed, Ref, ref} from "vue";
import apis from "../api/index.js";
import {useRoute} from "vue-router";
import {MODE_BOX, MODE_GOODS} from "../config";
import {formatNowDateTime} from "../utils/TimeUtil";

interface Goods {
  mode?: string
  name: string
  comment?: string
  status?: string
  updated_time: string
  created_time: string
  is_deleted?: string
}

interface GoodsTreeNode {
  label: string
  children: GoodsTreeNode[]
}

let goodsData: Ref<Goods[]> = ref([])
let deletedGoods: Ref<Goods[]> = ref([])

const defaultBoxName = 'Age'
let boxName: string = ''
const route = useRoute()

if (Object.keys(route.query).length != 0){
  boxName = route.query.boxName.toString()
} else {
  boxName = defaultBoxName
}

apis.getAllGoods(boxName).then(res =>{
  goodsData.value = res.data.data
  deletedGoods.value = goodsData.value
      .filter(goods => goods.is_deleted === true)
  goodsData.value = goodsData.value
      .filter(goods => goods.is_deleted !== true)
})

const goodsTree = computed(() => {
  return deletedGoods.value.map(goods => ({
    label: goods.name,
    children: [
      { label: `Status: ${goods.status}` },
      { label: `Updated time: ${goods.updated_time}` },
      { label: `Created time: ${goods.created_time}` },
      { label: `Comment: ${goods.comment}` }
    ]
  }));
});

defineProps({
  key: Number
})

const emit = defineEmits(['refresh-goods'])

const delGoods = (goodsName) => {
  console.log(goodsName)
  apis.deleteItem(MODE_GOODS, goodsName).then(res =>{
    emit('refresh-goods')
  })
}

const permanentlyDelGoods = (goodsName) => {
  apis.permanentlyDelete(MODE_GOODS, goodsName).then(res =>{
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
  created_time: null
})

let isAddGoodsForm = ref(false)

const onSubmitAddGoodsForm = () => {
  newGoods.value.updated_time = newGoods.value.created_time = formatNowDateTime()
  apis.addItem(newGoods).then(res =>{
    emit('refresh-goods')
  })
}
</script>

<template>
  <el-table :data="goodsData" style="width: 100%">
    <el-table-column prop="name" label="Name" width="180" />
    <el-table-column prop="status" label="Status" width="70" />
    <el-table-column prop="updated_time" label="Updated time" width="130" />
    <el-table-column prop="created_time" label="Created time" width="130" />
    <el-table-column prop="comment" label="Comment" width="200" />
    <el-table-column fixed="right" label="Operations" width="120">
      <template #default="scope">
        <el-button link type="primary" size="small" @click="delGoods(scope.row.name)">
          Delete
        </el-button>
      </template>
    </el-table-column>
  </el-table>

  <el-button @click="isAddGoodsForm = true">Add Goods</el-button>

  <el-form id="addBoxForm" v-show="isAddGoodsForm" :model="newGoods">
    <el-form-item label="Name">
      <el-input v-model="newGoods.name" />
    </el-form-item>
    <el-form-item label="Status">
      <el-input v-model="newGoods.status" />
    </el-form-item>
    <el-form-item label="Comment">
      <el-input v-model="newGoods.comment" type="textarea" autosize />
    </el-form-item>
    <el-button type="primary" @click="onSubmitAddGoodsForm">Create</el-button>
  </el-form>

<!--  Trash bin-->
  <el-collapse>
    <el-collapse-item title="Trash">
      <el-tree
        :data="goodsTree" :props="{ children: 'children', label: 'label' }"
        show-checkbox accordion>
      </el-tree>
    </el-collapse-item>
  </el-collapse>

<!--  <el-collapse accordion>-->
<!--    <el-collapse-item title="Trash">-->
<!--      <el-collapse>-->
<!--        <el-collapse-item v-for="goods in deletedGoods">-->
<!--          <template #title>-->
<!--            <el-col :span="18">-->
<!--              <div style="text-align: left">  {{goods.name}}</div>-->
<!--            </el-col>-->
<!--            <el-col :span="6"><div>-->
<!--                <el-popconfirm width="240" title="Are you sure to delete this?">-->
<!--                  <template #reference>-->
<!--                    <el-button type="danger" @click="permanentlyDelGoods(goods.name)">Delete</el-button>-->
<!--                  </template>-->
<!--                </el-popconfirm>-->
<!--                <el-button @click="restore(goods.name)">Restore</el-button>-->
<!--            </div></el-col>-->
<!--          </template>-->

<!--          <el-descriptions>-->
<!--            <el-descriptions-item label="Status">{{goods.status}}</el-descriptions-item>-->
<!--            <el-descriptions-item label="Updated time">{{goods.updated_time}}</el-descriptions-item>-->
<!--            <el-descriptions-item label="Created time">{{goods.created_time}}</el-descriptions-item>-->
<!--            <el-descriptions-item label="Comment">{{goods.comment}}</el-descriptions-item>-->
<!--          </el-descriptions>-->
<!--        </el-collapse-item>-->
<!--      </el-collapse>-->
<!--    </el-collapse-item>-->
<!--  </el-collapse>-->

</template>

<style scoped>

</style>