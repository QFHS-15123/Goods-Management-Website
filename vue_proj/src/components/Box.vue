<script setup name="BoxView" lang="ts">
  import {h, Ref, ref} from "vue";
  import apis from "../api/index.js";
  import { useRouter } from "vue-router";
  import { formatNowDateTime } from "../utils/TimeUtil"
  import { MODE_BOX } from "../config";
  import {ElNotification} from "element-plus";
  import Cookies from "js-cookie";
  import {Delete, Edit} from "@element-plus/icons-vue";
  import MyCell from './my-cell.vue';

  interface Box {
    mode?: string
    name: string
    comment?: string
    updated_time?: string
    created_time?: string
    is_deleted?: string
  }

  let boxData: Ref<Box[]> = ref([])
  let deletedBox: Array<string>

  apis.getAllBoxes().then(res =>{
    boxData.value = res.data.data
    deletedBox = boxData.value
      .filter(box => box.is_deleted === true)
      .map(box => box.name)
    boxData.value = boxData.value
        .filter(box => box.is_deleted !== true)
  })

  const changeBox = (boxName: string) => {
    Cookies.set('boxName', boxName)
    location.href = '/?boxName=' + boxName
  }

  defineProps({
    key: Number
  })

  const emit = defineEmits(['refresh-box'])

  const delBox = (boxName) => {
    apis.deleteItem(MODE_BOX, boxName).then(res =>{
      emit('refresh-box')
    })
  }

  let updateComponent: Ref<number> = ref(Date.now())

  let initialBoxName: string
  const setInitialBoxName = (boxName: string) => {
    initialBoxName = boxName
  };

  const updateBoxName = (newBoxName: string) => {
    console.log(newBoxName)
    apis.updateBox(initialBoxName, newBoxName, formatNowDateTime()).then(res =>{
      console.log(res)
    })
    // text.value = newText;
  };

  // let isEditBoxForm: Ref<boolean> = ref(false)
  // let editingBox: Ref<Box> = ref({
  //   name: null,
  //   comment: null
  // })
  // let beforeEditBox: Box
  //
  // const showEditBoxForm = (box: Box) => {
  //   isEditBoxForm.value = true
  //   console.log(isEditBoxForm.value)
  //   beforeEditBox = box
  //   editingBox = ref(Object.assign({}, box))
  //   console.log(editingBox.value)
  // }
  //
  // const handleEditFormInput = (col: string, value: string) => {
  //   if (beforeEditBox !== editingBox.value) {
  //     editingBox.value.updated_time = formatNowDateTime()
  //     apis.updateBox(editingBox.value.name, col, value, editingBox.value.updated_time).then(res =>{
  //       console.log(res)
  //     })
  //   }
  // }

  const permanentlyDelBox = (boxName) => {
    apis.permanentlyDelete(MODE_BOX, boxName).then(res =>{
      ElNotification({
        title: "Success",
        message: "Delete box successfully!",
        showClose: false
      })
      emit('refresh-box')
    })
  }

  const restore = (boxName) => {
    apis.restoreItem(MODE_BOX, boxName).then(res =>{
      emit('refresh-box')
    })
  }

  let newBox: Ref<Box> = ref({
    mode: MODE_BOX,
    name: null,
    comment: null,
    updated_time: null,
    created_time: null
  })

  let isAddBoxForm = ref(false)

  const onSubmitAddBoxForm = () => {
  newBox.value.updated_time = newBox.value.created_time = formatNowDateTime()
  apis.addBox(newBox).then(res =>{
    ElNotification({
      title: "Success",
      message: "Add box successfully!",
      showClose: false
    })
    emit('refresh-box')
  })
}

</script>

<template>

  <div v-for="box in boxData" :key="updateComponent">
    <div>
      <my-cell :initial-text="box.name" @dblclick="setInitialBoxName" @update:text="updateBoxName"></my-cell>
<!--      <el-button :key="box.name" text @click="changeBox(box.name)">{{ box.name }}</el-button>-->
<!--      <el-button  @click="delBox(box.name)"-->
<!--                  type="danger" :icon="Delete" circle />-->
<!--      <el-button @click="showEditBoxForm(box)"-->
<!--                 type="primary" :icon="Edit" circle />-->
    </div>
<!--    <div>-->
<!--      {{ box.comment }}-->
<!--    </div>-->
<!--    <el-form id="editBoxForm" v-if="isEditBoxForm" :model="editingBox">-->
<!--      <el-form-item label="Name">-->
<!--        <el-input v-model="editingBox.name" @input="handleEditFormInput('name', editingBox.name)"/>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="Comment">-->
<!--        <el-input v-model="editingBox.comment" @input="handleEditFormInput('comment', editingBox.comment)"-->
<!--                  type="textarea" autosize />-->
<!--      </el-form-item>-->
<!--    </el-form>-->
  </div>

  <el-collapse>
    <el-collapse-item title="Trash">
      <div v-for="boxName in deletedBox">
        <span>{{boxName}}</span>
        <span>
          <el-popconfirm width="240" title="Are you sure to delete this?">
            <template #reference>
              <el-button @click="permanentlyDelBox(boxName)">Delete</el-button>
            </template>
          </el-popconfirm>
        </span>
        <span><el-button @click="restore(boxName)">Restore</el-button></span>
      </div>
    </el-collapse-item>
  </el-collapse>

  <el-button @click="isAddBoxForm=true">Add Box</el-button>

    <el-form id="addBoxForm" v-show="isAddBoxForm" :model="newBox">
      <el-form-item label="Name">
        <el-input v-model="newBox.name" />
      </el-form-item>
      <el-form-item label="Comment">
        <el-input v-model="newBox.comment" type="textarea" autosize />
      </el-form-item>
      <el-button type="primary" @click="onSubmitAddBoxForm">Create</el-button>
    </el-form>
</template>

<style lang="scss">

</style>
