<script setup name="BoxView" lang="ts">
import {h, Ref, ref} from "vue";
import apis from "../api/index.js";
import { useRouter } from "vue-router";
import { formatNowDateTime } from "../utils/TimeUtil"
import { MODE_BOX } from "../config";
import {ElNotification} from "element-plus";
import {setCookie} from "../utils/CookieUtils.ts";

interface Box {
  mode?: string
  name: string
  comment?: string
  updated_time: string
  created_time: string
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

let $router = useRouter()
const changeBox = (e) => {
  const boxName = e.target.innerText
  $router.push({
    path: '/',
    query: { boxName: boxName }
  })
  location.reload()
  setCookie('boxName', boxName)
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

  <div v-for="box in boxData">
    <el-button :key="box.name" text @click="changeBox($event)">
      {{ box.name }}
    </el-button>
    <el-button @click="delBox(box.name)">Delete</el-button>
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
