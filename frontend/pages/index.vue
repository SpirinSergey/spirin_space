<template>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>

    <div>
    <p>Текущее значение: {{ counterStore.count }}</p>
    <button @click="counterStore.increment">Увеличить</button>
    <button @click="counterStore.decrement">Уменьшить</button>
  </div>

   <div>
    <h1 v-if="content">{{ content.title }}</h1>
    <p v-if="content">{{ content.description }}</p>
    <p v-else>Загрузка данных...</p>
  </div>
</template>

<script setup lang="ts">
import { useCounterStore } from '~/stores/useCounterStore'
import { useContent } from '~/composables/useContent'


const counterStore = useCounterStore()
const { content } = useContent()
</script>