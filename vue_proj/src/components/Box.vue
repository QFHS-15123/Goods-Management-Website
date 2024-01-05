<script setup name="BoxView" lang="ts">
import {Ref, ref} from "vue";
import apis from "../api/index.js";
import { useRouter } from "vue-router";
import { formatNowDateTime } from "../utils/TimeUtil"
import {MODE_BOX} from "../config";

interface Box {
  mode?: string
  name: string
  comment?: string
  updated_time: string
  created_time: string
  is_deleted?: string
}

let isDelPop:boolean[] = []

let boxData: Ref<Box[]> = ref([])

let deletedBox: Array<string> = []

apis.getAllBoxes().then(res =>{
  boxData.value = res.data.data
  console.log(boxData.value)
  let i: number
  for (i = 0; i<boxData.value.length; i++){
    if (boxData.value[i].is_deleted === true){
     deletedBox.push(boxData.value[i].name)
    }
  }
  console.log(deletedBox)
  for (i = 0; i<boxData.value.length; i++){
    isDelPop[i] = false
  }
})

let $router = useRouter()
const changeBox = (val) => {
    $router.push({
    path: '/goods',
    query: { boxName: val.target.innerText}
  })
}

const delBox = (boxName) => {
  apis.deleteItem(MODE_BOX, boxName).then(res =>{
    console.log(res)
    location.reload()
  })
}

const permanentlyDelBox = (boxName) => {
  apis.permanentlyDelete(MODE_BOX, boxName).then(res =>{
    console.log(res)
    location.reload()
  })
}

let newBox: Ref<Box> = ref({
  mode: MODE_BOX,
  name: null,
  comment: null,
  updated_time: null,
  created_time: null
})

let isAddBoxForm = ref(false)

const onSubmitForm = () => {
  newBox.value.updated_time = newBox.value.created_time = formatNowDateTime()
  apis.addItem(newBox).then(res =>{
    console.log(res)
  })
}
</script>

<template>

  <div v-for="(box,idx) in boxData">
    <el-button :key="box.name" text @click="changeBox($event)">
      {{ box.name }}
    </el-button>
    <el-button @click="delBox(box.name)">Delete</el-button>

  </div>

  <!--    <el-popover :visible="isDelPop[idx]" placement="top" :width="160">-->
<!--      <p>Are you sure to delete this?</p>-->
<!--      <div style="text-align: right; margin: 0">-->
<!--        <el-button size="small" text @click="isDelPop[idx] = false">cancel</el-button>-->
<!--        <el-button size="small" type="primary" @click="isDelPop[idx] = false">confirm</el-button>-->
<!--      </div>-->
<!--      <template #reference>-->
<!--        <el-button @click="isDelPop[idx] = true">Delete</el-button>-->
<!--      </template>-->
<!--    </el-popover>-->

      <el-collapse>
      <el-collapse-item title="Trash">
        <div v-for="boxName in deletedBox">
          <span>{{boxName}}</span>
          <span>
            <el-popconfirm
                width="240"
                title="Are you sure to delete this?">
              <template #reference>
                <el-button @click="permanentlyDelBox(boxName)">Delete</el-button>
              </template>
            </el-popconfirm>
          </span>
        </div>
      </el-collapse-item>
    </el-collapse>

  <el-button @click="isAddBoxForm=true">Add Box</el-button>

  <el-form id="addBoxForm" v-show="isAddBoxForm" :model="newBox">
    <el-form-item label="Name">
      <el-input v-model="newBox.name" />
    </el-form-item>
    <el-form-item label="Comment">
      <el-input v-model="newBox.comment" type="textarea" autosize />
    </el-form-item>
    <el-button type="primary" @click="onSubmitForm">Create</el-button>
  </el-form>

</template>

<style lang="scss">

</style>
