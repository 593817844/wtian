<template>
  <a-layout class="layout">
    <a-layout-header class="header">
      <div class="logo">问天易经AI</div>
      <a-menu
        v-model:selectedKeys="current"
        theme="dark"
        mode="horizontal"
        :style="{ lineHeight: '64px' }"
        class="transparent-menu"
      >
        <a-menu-item key="home" @click="goToRoute('Home')">
          <template #icon><HomeOutlined /></template>
          首页
        </a-menu-item>
        <a-menu-item key="bazi" @click="goToRoute('Bazi')">
          <template #icon><CalculatorOutlined /></template>
          八字测算
        </a-menu-item>
        <a-menu-item key="guagua" @click="goToRoute('Gua')">
          <template #icon><CompassOutlined /></template>
          64卦占卜
        </a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content class="content">
      <a-breadcrumb style="margin: 16px 0; font-size: 14px;">
        <a-breadcrumb-item>Home</a-breadcrumb-item>
        <a-breadcrumb-item>{{ route.name }}</a-breadcrumb-item>
      </a-breadcrumb>
      <div class="content-wrapper">
        <router-view />
      </div>
    </a-layout-content>
    <a-layout-footer class="footer">
      Your Footer Information Here
    </a-layout-footer>
  </a-layout>
</template>

<script setup>
import { ref, computed } from 'vue';
import { HomeOutlined, CalculatorOutlined, CompassOutlined } from '@ant-design/icons-vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();

const current = computed(() => {
  return [route.name || 'home']; // Use 'home' as the key to match the menu
});

const goToRoute = (routeName) => {
  router.push({ name: routeName });
};
</script>

<style scoped>
.layout {
  min-height: 100vh;
  background: #f0f2f5; /* Light background for the entire layout */
}

/* Header Styling */
.header {
  background: linear-gradient(90deg, #1e3a8a, #3b82f6); /* Gradient header */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.logo {
  float: left;
  width: auto;
  height: 31px;
  margin: 16px 24px 16px 0;
  color: white;
  text-align: center;
  line-height: 31px;
  font-size: 22px;
  font-weight: bold;
  padding: 0 12px;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.05); /* Slight zoom effect on hover */
}

/* Transparent Menu */
.transparent-menu {
  background: transparent !important;
  border-bottom: none;
}

.transparent-menu .ant-menu-item {
  color: rgba(255, 255, 255, 0.9);
  font-size: 16px;
  transition: all 0.3s ease;
}

.transparent-menu .ant-menu-item:hover {
  color: white;
  background: rgba(255, 255, 255, 0.15) !important;
}

.transparent-menu .ant-menu-item-selected {
  color: white !important;
  background: rgba(255, 255, 255, 0.2) !important;
  border-bottom: 2px solid white;
}

/* Content Styling */
.content {
  padding: 0 50px; /* Default padding for larger screens */
  margin-top: 24px;
}

.content-wrapper {
  background: #ffffff;
  padding: 32px;
  min-height: 280px;
  margin: 0 50px; /* Default margin for larger screens */
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05); /* Subtle shadow for depth */
  transition: box-shadow 0.3s ease;
}

.content-wrapper:hover {
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1); /* Enhanced shadow on hover */
}

/* Footer Styling */
.footer {
  text-align: center;
  background: #ffffff;
  color: #666;
  padding: 24px 50px;
  font-size: 14px;
  border-top: 1px solid #e8e8e8;
}

/* Responsive Design: Remove padding and margins on smaller screens */
@media (max-width: 768px) {
  .content {
    padding: 0; /* Remove padding on smaller screens */
  }

  .content-wrapper {
    margin: 0; /* Remove margin on smaller screens */
    border-radius: 0; /* Remove rounded corners for full-width */
    box-shadow: none; /* Remove shadow on mobile for cleaner look */
  }

  .header {
    padding: 0 16px; /* Adjust header padding for mobile */
  }

  .logo {
    font-size: 18px;
    margin: 16px 16px 16px 0;
  }

  .transparent-menu .ant-menu-item {
    font-size: 14px; /* Smaller font for mobile */
  }

  .footer {
    padding: 16px;
  }
}

/* Dark Theme Adjustments */
[data-theme='dark'] .layout {
  background: #1f1f1f;
}

[data-theme='dark'] .content-wrapper {
  background: #2d2d2d;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

[data-theme='dark'] .footer {
  background: #2d2d2d;
  color: #aaa;
  border-top: 1px solid #444;
}
</style>