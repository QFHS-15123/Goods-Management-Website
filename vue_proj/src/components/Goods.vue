<script setup name="GoodsView" lang="ts">
import {ref} from "vue";
import apis from "../api/index.js";
import {useRoute} from "vue-router";

interface Goods {
  mode?: string
  name: string
  comment?: string
  status?: string
  updated_time: string
  created_time: string
  is_deleted?: string
}

let goodsData = ref([])

const defaultBoxName = 'Age'
let boxName:string = ''
const route = useRoute()

if (Object.keys(route.query).length != 0){
  boxName = route.query.boxName.toString()
} else {
  boxName = defaultBoxName
}

apis.getAllGoods(boxName)
    .then(res =>{
      goodsData.value = res.data.data
    })

const addGoods = () => {

}
</script>

<template>
  <el-table :data="goodsData" style="width: 100%">
    <el-table-column prop="name" label="Name" width="180" />
    <el-table-column prop="status" label="Status" width="70" />
    <el-table-column prop="updated_time" label="Updated time" width="130" />
    <el-table-column prop="created_time" label="Created time" width="130" />
    <el-table-column prop="comment" label="Comment" width="200" />
  </el-table>
  <el-button @click="addGoods">Add Goods</el-button>

</template>

<style scoped>

</style>