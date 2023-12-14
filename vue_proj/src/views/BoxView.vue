<script setup name="BoxView">
import { ref } from "vue";
import apis from "../api/index.js";
import { useRouter } from "vue-router";

let boxData = ref([])
apis.get_all_boxes()
    .then(res =>{
      boxData.value = res.data.data
    })

let $router = useRouter()
function handleCurrentChange(currentRow){
  console.log(1)
  console.log(currentRow.name)
  $router.push({
    path: '/goods',
    query: { boxName: currentRow.name}
  })
}
</script>

<template>
<div>
  <el-table :data="boxData"
            highlight-current-row
            @current-change="handleCurrentChange"
            style="width: 100%">
    <el-table-column prop="name" label="Name" width="180" />
    <el-table-column prop="updated_time" label="Updated time" width="180" />
    <el-table-column prop="created_time" label="Created time" width="180" />
    <el-table-column prop="comment" label="Comment" />
  </el-table>
</div>
</template>

<style scoped>

</style>