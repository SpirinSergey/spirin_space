import { ref, onMounted } from "vue";

interface ContentData {
  title: string;
  description: string;
}

export const useContent = () => {
  const content = ref<ContentData | null>(null);

  const loadContent = async () => {
    try {
      const response = await fetch("/content.json");
      content.value = await response.json();
    } catch (error) {
      console.error("Ошибка загрузки JSON:", error);
    }
  };

  onMounted(loadContent);

  return {
    content,
  };
};
