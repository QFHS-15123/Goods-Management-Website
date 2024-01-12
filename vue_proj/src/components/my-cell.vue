<script setup name="MyCell" lang="ts">
import {ref, defineProps, defineEmits, nextTick, onMounted} from 'vue';

  const props = defineProps({
    initialText: String
  });


  const emits = defineEmits(['update:text', 'dblclick']);

  const text = ref(props.initialText); // Use initialText as the initial value
  const isEditing = ref(false);
  const input = ref()

  const enableEditing = async () => {
    isEditing.value = true;
    await nextTick()  // Rendering components takes time and is not as fast as typescript execution.
    input.value.focus();
    emits('dblclick', props.initialText);
  };

  const disableEditing = () => {
    isEditing.value = false;
  };

  const handleInputChange = (e: InputEvent) => {
    text.value = (e.target as HTMLInputElement).value;
    emits('update:text', text.value);
  };
</script>

<template>
  <div v-if="!isEditing" @dblclick="enableEditing">{{ text }}</div>
  <input
    v-else
    type="text"
    v-model="text"
    @blur="disableEditing"
    @keyup.enter="disableEditing"
    v-on:input="handleInputChange"
    ref="input"
  />
</template>
