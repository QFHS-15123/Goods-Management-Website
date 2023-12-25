<script setup name="BoxView" lang="ts">
import {Ref, ref} from "vue";
import apis from "../api/index.js";
import { useRouter } from "vue-router";

interface Box {
  name: string
  comment?: string
  updated_time: string
  created_time: string
}

let isDelPop:boolean[] = []

let boxData: Ref<Box[]> = ref([])
apis.get_all_boxes().then(res =>{
  boxData.value = res.data.data
  let i:number
  for (i = 0; i<boxData.value.length; i++){
    isDelPop[i] = false
  }
  console.log(isDelPop)
})

let $router = useRouter()
const changeBox = (val) => {
    $router.push({
    path: '/goods',
    query: { boxName: val.target.innerText}
  })
}

let newBox: Ref<Box> = ref({
  name: null,
  comment: null,
  updated_time: null,
  created_time: null
})

let isAddBoxForm = ref(false)

const onSubmitForm = () => {
  let currentDate = new Date()
  let date = currentDate.toLocaleDateString()
  newBox.value.updated_time = String(date)
  newBox.value.created_time = String(date)
  apis.add_box(newBox).then(res =>{
    console.log(res)
  })
}
</script>

<template>

  <div v-for="(box,idx) in boxData">
    <el-button :key="box.name" text @click="changeBox($event)">
      {{ box.name }}
    </el-button>

    <el-popover :visible="isDelPop[idx]" placement="top" :width="160">
      <p>Are you sure to delete this?</p>
      <div style="text-align: right; margin: 0">
        <el-button size="small" text @click="isDelPop[idx] = false">cancel</el-button>
        <el-button size="small" type="primary" @click="isDelPop[idx] = false">confirm</el-button>
      </div>
      <template #reference>
        <el-button @click="isDelPop[idx] = true">Delete</el-button>
      </template>
    </el-popover>
  </div>

  <el-button @click="isAddBoxForm=true">Add Box</el-button>

  <el-form id="addBoxForm" v-show="isAddBoxForm" :model="newBox">
    <el-form-item label="Name">
      <el-input v-model="newBox.name" />
    </el-form-item>
    <el-form-item label="Comment">
      <el-input v-model="newBox.comment" type="textarea" autosize />
    </el-form-item>
    <el-button type="primary" @click="onSubmitForm">Create</el-button>
  </el-form>

</template>

<style lang="scss">

</style>
