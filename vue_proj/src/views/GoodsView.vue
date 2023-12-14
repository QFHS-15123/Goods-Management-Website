<script setup name="GoodsView">
import { ref } from "vue";
import apis from "../api/index.js";
import { useRoute } from "vue-router";

const route = useRoute()
let boxName = route.query.boxName

let goodsData = ref([])

apis.get_all_goods(boxName)
    .then(res =>{
      goodsData.value = res.data.data
    })

</script>

<template>
<div>
  <el-table
      :data="goodsData"
      style="width: 100%">
    <el-table-column prop="name" label="Name" width="180" />
    <el-table-column prop="status" label="Status" width="180" />
    <el-table-column prop="updated_time" label="Updated time" width="180" />
    <el-table-column prop="created_time" label="Created time" width="180" />
    <el-table-column prop="comment" label="Comment" />
  </el-table>
</div>
</template>

<style scoped>

</style>