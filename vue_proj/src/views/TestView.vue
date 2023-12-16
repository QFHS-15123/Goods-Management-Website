<script setup name="BoxView" lang="ts">
import { useRouter } from "vue-router";

interface Box {
  name: string
  comment?: string
  updated_time: string
  created_time: string
}

const boxData =
[
    {
        "name": "Age",
        "comment": "年龄",
        "updated_time": "2023/10/12",
        "created_time": "2023/10/7"
    },
    {
        "name": "Department",
        "comment": "在当前公司的工作年数",
        "updated_time": "2023/10/13",
        "created_time": "2023/10/8"
    },
    {
        "name": "EmployeeCount",
        "comment": "所属部门",
        "updated_time": "2023/10/14",
        "created_time": "2023/10/9"
    },
    {
        "name": "TESTBOX",
        "comment": "AKATEST",
        "updated_time": "2023/9/14",
        "created_time": "2023/9/10"
    }
]

</script>

<template>
  <el-row>
    <el-col :span="24"><div class="grid-content ep-bg-purple-dark" /><el-card>111</el-card></el-col>
  </el-row>
  <el-row>
    <el-col :span="12"><div class="grid-content ep-bg-purple" /><el-card>111</el-card></el-col>
    <el-col :span="12"><div class="grid-content ep-bg-purple-light" /><el-card>111</el-card></el-col>
  </el-row>
  <el-row>
    <el-col :span="8"><div class="grid-content ep-bg-purple" /><el-card>111</el-card></el-col>
    <el-col :span="8"><div class="grid-content ep-bg-purple-light" /><el-card>111</el-card></el-col>
    <el-col :span="8"><div class="grid-content ep-bg-purple" /><el-card>111</el-card></el-col>
  </el-row>
  <el-row>
    <el-col :span="6"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="6"><div class="grid-content ep-bg-purple-light" /></el-col>
    <el-col :span="6"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="6"><div class="grid-content ep-bg-purple-light" /></el-col>
  </el-row>
  <el-row>
    <el-col :span="4"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple-light" /></el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple-light" /></el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple-light" /></el-col>
  </el-row>
</template>

<style lang="scss">
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>


<!--<template>-->
<!--  -->
<!--  <el-row :gutter="20" class="el-row">-->
<!--    <el-col :span="8" v-for="box in boxData" :key="box.name" :data="boxData">-->
<!--    <el-card class="el-card">-->
<!--      <div slot="body">-->
<!--        {{ box.name }}-->
<!--      </div>-->

<!--      <div slot="footer" class="card-footer">-->
<!--        <span>Created: {{ box.created_time }}</span>-->
<!--        <span>Updated: {{ box.updated_time }}</span>-->
<!--      </div>-->
<!--    </el-card>-->
<!--    </el-col>-->
<!--  </el-row>-->

<!--</template>-->

<!--<style scoped>-->
<!--.el-row {-->
<!--  display: flex;-->
<!--  margin-bottom: 20px;-->
<!--  flex-wrap: wrap-->
<!--}-->

<!--.el-card {-->
<!--  min-width: 100%;-->
<!--  height: 100%;-->
<!--  margin-right: 20px;-->
<!--  transition: all .5s;-->
<!--}-->

<!--.card-container {-->
<!--  display: flex;-->
<!--  flex-wrap: wrap;-->
<!--  justify-content: space-between;-->
<!--}-->

<!--.box-card {-->
<!--  width: calc(33.333% - 20px); /* Adjust for 3 cards per row with some spacing */-->
<!--  margin-bottom: 20px;-->
<!--}-->

<!--.card-footer {-->
<!--  display: flex;-->
<!--  justify-content: space-between;-->
<!--}-->
<!--</style>-->
