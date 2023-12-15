<script setup name="BoxView" lang="ts">
import {Ref, ref} from "vue";
import apis from "../api/index.js";
import { useRouter } from "vue-router";
import { ElMessageBox } from "element-plus";
import { Plus } from "@element-plus/icons-vue";

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

let boxData: Ref<Box[]> = ref([])

apis.get_all_boxes().then(res =>{
  boxData.value = res.data.data
})


let $router = useRouter()
const handleCurrentChange = (val: Box | undefined) => {
  $router.push({
    path: '/goods',
    query: { boxName: val.name}
  })
}

const addBox = () => {
  const newRow: Box = {
    name: null,
    comment: null,
    updated_time: null,
    created_time: null
  }
  boxData.value.push(newRow)
}

// const dialogVisible = ref(false)

// const handleClose = (done: () => void) => {
//   ElMessageBox.confirm('Are you sure to close this dialog?')
//     .then(() => {
//       done()
//     })
//     .catch(() => {
//       // catch error
//     })
// }

</script>

<template>
  <div>
    <el-container>
      <el-header>Header</el-header>

      <el-container>

        <el-main>
<!--          <el-button-->
<!--            type="primary" :icon="Plus" circle-->
<!--            @click="dialogVisible = true">-->
<!--          </el-button>-->

          <div>
            <el-table :data="boxData"
            highlight-current-row
            @current-change="handleCurrentChange"
            style="width: 100%">
              <el-table-column type="index" width="50" />
                <el-table-column
                  v-for="col in boxColNames"
                  :prop="col.prop"
                  :label="col.label"
                  :key="col.prop"
                  width="180"
                />
              <el-table-column>
                <el-button @click="addBox">Add</el-button>
              </el-table-column>
            </el-table>
          </div>

        </el-main>

      </el-container>

    </el-container>

  </div>

</template>

<style scoped>

</style>


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