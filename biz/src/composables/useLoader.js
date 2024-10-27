// src/composables/useLoader.js
import { ref } from 'vue';

const isVisible = ref(false);

export function useLoader() {
  const showLoader = () => {
    isVisible.value = true;
  };

  const hideLoader = () => {
    isVisible.value = false;
  };

  return { isVisible, showLoader, hideLoader };
}
