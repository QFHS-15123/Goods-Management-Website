<script setup name="BoxView">
import {onBeforeMount} from "vue";
import boxApi from "../api/index.js";

let boxs = {}
onBeforeMount(() => {
  boxApi.get_all_boxes()
      .then(res =>{
        console.log(res.data)
        boxs = res.data
      })
});
</script>

<template>
<div>
  <el-text>
    boxs: {{ boxs }}
  </el-text>
</div>
</template>

<style scoped>

</style>