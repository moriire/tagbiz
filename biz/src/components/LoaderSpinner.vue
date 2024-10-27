<!-- src/components/Loader.vue -->
<template>
    <Teleport to="body">
      <div v-if="isVisible" class="loader-overlay d-flex justify-content-center align-items-center">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    </Teleport>
  </template>
  
  <script setup>
  import { useLoader } from '../composables/useLoader.js';
  
  const { isVisible } = useLoader();
  </script>
  
  <style scoped>
  .loader-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(9, 6, 6, 0.8);
    z-index: 1050; /* Ensures it stays above other content */
  }
  </style>
  