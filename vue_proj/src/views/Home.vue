<script setup name="Home">
  import {ref} from "vue";
  import BoxView from '../components/Box.vue'
  import GoodsView from '../components/Goods.vue'
  import {useRoute, useRouter} from "vue-router";
  import api from "../api/index.js";
  import Cookies from "js-cookie";

  const $router = useRouter()
  const route = useRoute()
  if (Object.keys(route.query).length === 0){
    console.log(1)
    Cookies.set('boxName', 'Age')
    const boxName = Cookies.get('boxName')
    console.log(boxName)
    // $router.push({
    //   path: '/',
    //   query: { boxName: boxName }
    // })
  }

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