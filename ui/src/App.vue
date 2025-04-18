<template>
  <div class="container">
    <a-menu
      v-model:selectedKeys="current"
      mode="horizontal"
      :items="items"
      class="menu"
    />

    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { h, ref, computed } from 'vue';
import { HomeOutlined, CalculatorOutlined, CompassOutlined } from '@ant-design/icons-vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();

const current = computed(() => {
  return [route.name || 'Home'];
});

const items = ref([
  {
    key: 'home',
    icon: () => h(HomeOutlined),
    label: '首页',
    title: '首页',
    onClick: () => router.push({ name: 'Home' }),
  },
  {
    key: 'bazi',
    icon: () => h(CalculatorOutlined),
    label: '八字测算',
    title: '八字测算',
    onClick: () => router.push({ name: 'Bazi' }),
  },
  {
    key: 'guagua',
    icon: () => h(CompassOutlined),
    label: '64卦占卜',
    title: '64卦占卜',
    onClick: () => router.push({ name: 'Gua' }),
  },
]);
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column; /* Arrange menu and content vertically */
  align-items: center; /* Center the menu and content horizontally */
  width: 100%;
  padding: 20px;
  box-sizing: border-box; /* Include padding in the width calculation */
}

.menu {
  width: 80%; /* Adjust as needed */
  max-width: 1200px;
  margin-bottom: 20px;
  border: none; /* Remove default border */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Add subtle shadow */
  border-radius: 8px; /* Add rounded corners */
  background-color: #f8f8f8; /* Light background color */
}

/* Style the menu items */
.ant-menu-item {
  padding: 0 24px;
  font-size: 16px;
  font-weight: 500;
  color: #333;
}

.ant-menu-item:hover {
  color: #007bff; /* Hover color */
}

.ant-menu-item-selected {
  color: #fff !important;
  background-color: #007bff !important;
}

.ant-menu-item-selected:hover {
  color: #fff !important;
}

/* Style the icons */
.ant-menu-item .anticon {
  margin-right: 8px;
  font-size: 18px;
}


.content {
  width: 80%; /* Match menu width */
  max-width: 1200px; /* Match menu max-width */
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h1 {
  margin-bottom: 20px;
  color: #333;
}

section {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 5px;
}

p {
  line-height: 1.6;
  color: #555;
}
</style>
