import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/reset.css'; // 引入 Ant Design Vue 的 CSS reset

const app = createApp(App);
app.use(Antd);
app.use(router);
app.mount('#app');