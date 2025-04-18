import { createRouter, createWebHistory } from 'vue-router';
import Bazi from '../components/BaziView.vue';
import Gua from '../components/GuaView.vue';
import Home from '../components/HomeView.vue';

const routes = [
  {
    path: '/',
    redirect: { name: 'Home' } 
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/bazi',
    name: 'Bazi',
    component: Bazi
  },
  {
    path: '/gua',
    name: 'Gua',
    component: Gua
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;