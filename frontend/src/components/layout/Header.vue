<script setup>
import Container from "../shared/Container.vue";
</script>

<template>
  <nav class="mb-10 bg-slate-300">
    <Container>
      <div class="mx-2 flex flex-row py-6">
        <div class="basis-auto px-2">
          <RouterLink to="/">Главная страница</RouterLink>
        </div>
        <div class="basis-auto px-2">
          <RouterLink to="/about">Обо мне</RouterLink>
        </div>
        <div class="basis-auto px-2">
          <RouterLink to="/gallery">Галерея</RouterLink>
        </div>
      </div>
    </Container>
  </nav>
</template>
<style>
.router-link-active {
  color: blue;
}
</style>
