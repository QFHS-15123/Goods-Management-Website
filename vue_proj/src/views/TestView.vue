<script setup name="my-cell" lang="ts">
import MyCell from '../components/my-cell.vue';
import {ref} from "vue"; // Ensure correct import statement

const text = ref("the text");

const updateText = (newText: string) => {
  console.log(newText)
  text.value = newText;
};
</script>

<template>
  <my-cell :initial-text="text" @update:text="updateText"></my-cell>

  <div>{{text}}</div>
</template>
