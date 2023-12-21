<script setup name="BoxView" lang="ts">
import {Ref, ref} from "vue";
import apis from "../api/index.js";
import { useRouter } from "vue-router";
import {ElMessageBox, TableColumnCtx} from "element-plus";
import { Plus } from "@element-plus/icons-vue";
import {FALSE} from "sass";

interface Box {
  name: string
  comment?: string
  updated_time: string
  created_time: string
}

const boxColNames = [
  { prop: "name", label: 'Name' },
  { prop: "comment", label: 'Comment' },
  { prop: "updated_time", label: 'Updated Time' },
  { prop: "created_time", label: 'Created Time' }
]

const newRow: Box = {
  name: null,
  comment: null,
  updated_time: null,
  created_time: null
}

// let boxData: Ref<Box[]> = ref([])
//
// apis.get_all_boxes().then(res =>{
//   // boxData.value.push(newRow)
//   // boxData.value.push(...res.data.data)
//   boxData.value = res.data.data
//   boxData.value.push(newRow)
//
// })

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

let $router = useRouter()
const handleCurrentChange = (val: Box | undefined) => {
  $router.push({
    path: '/goods',
    query: { boxName: val.name}
  })
}

// const addBox = () => {
//   boxData.value.push(newRow)
// }

let isForm = false

</script>

<template>
    <el-button @click="isForm=true">Add Box</el-button>

  <el-dialog
    v-model="dialogVisible"
    title="Tips"
    width="30%"
    :before-close="handleClose"
  >
    <span>This is a message</span>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogVisible = false">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
<!--  <el-row :gutter="20">-->
<!--    <el-col :span="8" v-for="box in boxData" :key="box.name" :data="boxData">-->
<!--      <div class="box-container">-->
<!--        <div class="name-container">{{ box.name }}</div>-->
<!--&lt;!&ndash;        <el-divider />&ndash;&gt;-->
<!--        <div class="comment-container">{{ box.comment }}</div>-->
<!--      </div>-->
<!--      </el-col>-->
<!--  </el-row>-->
</template>

<style lang="scss">
.box-container {
  width: 100%;
  height: 0;
  padding-bottom: 100%;
  //display: flex;
  //flex-direction: column;
  border-style: solid;
  margin-right: 20px;
  margin-bottom: 20px;
  text-align: start;
}

.name-container, .comment-container {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: end;
}


</style>
<!--  <div class="card-container">-->
<!--    <el-card shadow="hover">-->
<!--      <div class="el-card-container">-->
<!--&lt;!&ndash;    <el-card&ndash;&gt;-->
<!--&lt;!&ndash;      v-for="box in boxData"&ndash;&gt;-->
<!--&lt;!&ndash;      :key="box.name"&ndash;&gt;-->
<!--&lt;!&ndash;      class="box-card"&ndash;&gt;-->
<!--&lt;!&ndash;    >&ndash;&gt;-->
<!--        <div class="el-card-body">-->
<!--          {{ box.name }}-->
<!--        </div>-->

<!--  &lt;!&ndash;      <template #footer class="el-card-footer">&ndash;&gt;-->
<!--        <div class="el-card-footer">aaa</div>-->
<!--  &lt;!&ndash;        <div>Created: {{ box.created_time }}</div>&ndash;&gt;-->
<!--  &lt;!&ndash;        <div>Updated: {{ box.updated_time }}</div>&ndash;&gt;-->
<!--  &lt;!&ndash;        </template>&ndash;&gt;-->
<!--      </div>-->
<!--    </el-card>-->

<!--  </div>-->
<!--  <div>-->
<!--    <el-container>-->
<!--      <el-header>Header</el-header>-->

<!--      <el-container>-->

<!--        <el-main>-->
<!--&lt;!&ndash;          <el-button&ndash;&gt;-->
<!--&lt;!&ndash;            type="primary" :icon="Plus" circle&ndash;&gt;-->
<!--&lt;!&ndash;            @click="dialogVisible = true">&ndash;&gt;-->
<!--&lt;!&ndash;          </el-button>&ndash;&gt;-->

<!--          <div>-->
<!--            <el-table :data="boxData"-->
<!--            highlight-current-row-->
<!--            @current-change="handleCurrentChange"-->
<!--            style="width: 100%">-->
<!--              <el-table-column type="index" width="50" />-->
<!--                <el-table-column-->
<!--                  v-for="col in boxColNames"-->
<!--                  :prop="col.prop"-->
<!--                  :label="col.label"-->
<!--                  :key="col.prop"-->
<!--                  width="180"-->
<!--                />-->
<!--              <template #append>-->
<!--                <el-row>-->
<!--                  <el-button @click="addBox">Your Button Text</el-button>-->
<!--                </el-row>-->
<!--              </template>-->
<!--&lt;!&ndash;              <el-table-column label="Action" width="180">&ndash;&gt;-->
<!--&lt;!&ndash;                <template #default="scope">&ndash;&gt;-->
<!--&lt;!&ndash;                  <el-button v-if="scope.$index === boxData.length - 1" type="primary">&ndash;&gt;-->
<!--&lt;!&ndash;                    Button Text&ndash;&gt;-->
<!--&lt;!&ndash;                  </el-button>&ndash;&gt;-->
<!--&lt;!&ndash;                </template>&ndash;&gt;-->
<!--&lt;!&ndash;              </el-table-column>&ndash;&gt;-->
<!--&lt;!&ndash;              <el-table-column>&ndash;&gt;-->
<!--&lt;!&ndash;                <el-button @click="addBox">Add</el-button>&ndash;&gt;-->
<!--&lt;!&ndash;              </el-table-column>&ndash;&gt;-->
<!--            </el-table>-->
<!--          </div>-->

<!--        </el-main>-->

<!--      </el-container>-->

<!--    </el-container>-->

<!--  </div>-->




<!--          <div>-->
<!--            <el-dialog-->
<!--              v-model="dialogVisible"-->
<!--              title="Tips"-->
<!--              width="30%"-->
<!--              draggable-->
<!--              :before-close="handleClose">-->
<!--              <span>This is a message</span>-->
<!--              <template #footer>-->
<!--                <span class="dialog-footer">-->
<!--                  <el-button @click="dialogVisible = false">Cancel</el-button>-->
<!--                  <el-button type="primary" @click="dialogVisible = false">-->
<!--                    Confirm-->
<!--                  </el-button>-->
<!--                </span>-->
<!--              </template>-->
<!--            </el-dialog>-->
<!--          </div>-->