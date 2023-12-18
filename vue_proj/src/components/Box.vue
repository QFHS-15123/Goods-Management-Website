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

let boxData: Ref<Box[]> = ref([])
apis.get_all_boxes().then(res =>{
  boxData.value = res.data.data
})

let $router = useRouter()
const changeBox = (val) => {
    $router.push({
    path: '/goods',
    query: { boxName: val.target.innerText}
  })
}

let newBox: Box = {
  name: null,
  comment: null,
  updated_time: null,
  created_time: null
}

let isForm = false
const onSubmit = () => {
  console.log('submit!')
}
</script>

<template>
  <el-button v-for="box in boxData" :key="box.name" text @click="changeBox($event)">
    {{ box.name }}
  </el-button>

  <el-button @click="isForm = true">Add Box</el-button>

  <el-form v-show="isForm" :model="newBox">
    <el-form-item label="Name">
      <el-input v-model="newBox.name" />
    </el-form-item>
    <el-form-item label="Comment">
      <el-input v-model="newBox.comment" />
    </el-form-item>
    <el-button type="primary" @click="onSubmitForm">Create</el-button>
  </el-form>
</template>

<style lang="scss">

</style>
