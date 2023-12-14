<script setup name="BoxView">
import { ref } from "vue";
import boxApi from "../api/index.js";


let boxData = ref([])
boxApi.get_all_boxes()
    .then(res =>{
      boxData.value = res.data.data
    })
</script>

<template>
<div>
  <el-table :data="boxData" style="width: 100%">
    <el-table-column prop="name" label="Name" width="180" />
    <el-table-column prop="updated_time" label="Updated time" width="180" />
    <el-table-column prop="created_time" label="Created time" width="180" />
    <el-table-column prop="comment" label="Comment" />
  </el-table>

</div>
</template>

<style scoped>

</style>