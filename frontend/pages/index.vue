<template>
  <Container>
    <h1 class="text-3xl font-bold underline">Hello world! rrr</h1>
    <NuxtLink to="/about">about page</NuxtLink>
  </Container>
</template>

<script setup lang="ts">
import { useCounterStore } from "~/stores/useCounterStore";
import { useContent } from "~/composables/useContent";

const counterStore = useCounterStore();
const { content } = useContent();
</script>
