<script setup name="Home">
import {ref} from "vue";
import BoxView from '../components/Box.vue'
import GoodsView from '../components/Goods.vue'

const drawer = ref(false)
const boxKeyView = ref(0)
const goodsKeyView = ref(0)

const refreshBoxView = () => {
  boxKeyView.value++
}

const refreshGoodsView = () => {
  goodsKeyView.value++
}

</script>

<template>
  <el-button type="primary" @click="drawer = true">Open Another Box</el-button>
  <GoodsView :key="goodsKeyView" @refresh-goods="refreshGoodsView" />

     <el-drawer v-model="drawer" title="Boxes">
       <BoxView :key="boxKeyView" @refresh-box="refreshBoxView"/>
  <!--  :before-close="handleClose"-->
    </el-drawer>
</template>

<style scoped>

</style>