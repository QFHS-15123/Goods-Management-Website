<script setup name="HelloWorld">
import userApi from '../api/index'
import { getCurrentInstance, onBeforeMount, ref } from 'vue'

const user = {
  username: "QFHS",
  password: "15123",
}

// let { proxy } = getCurrentInstance();

onBeforeMount(() => {
  userApi.login(user)
      .then(res =>{
        console.log(res.data)
      })
  // proxy.$http
  //   .post("/api/login", {
  //     user: "QFHS",
  //     password: "15123",
  //   })
  //   .then(function(res) {
  //     console.log(res.data)
  //   })
  //   .catch(function(error) {
  //     console.log(error);
  //   });
});

defineProps({
  msg: String,
})

const count = ref(0)
</script>

<template>

  <h1>{{ msg }}</h1>

  <div>
    <el-button type="primary">A Lonely Button</el-button>
  </div>

  <div>Username: {{ user.username }}</div>
  <div>Password: {{ user.password }}</div>

  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
    >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
