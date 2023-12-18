<script setup name="HomeView" lang="ts">
import {Ref, ref} from "vue";
import {useRoute, useRouter} from "vue-router";
import { Plus } from '@element-plus/icons-vue'

const drawer = ref(false)


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

   <el-drawer v-model="drawer" title="Boxes">
  <!--  :before-close="handleClose"-->

  </el-drawer>
</template>

<style scoped>

</style>