<template>
  <a-card title="易经占卜">
    <a-form :model="formState" @finish="onFinish" layout="vertical">
      <a-form-item label="性别" name="gender">
        <a-select v-model:value="formState.gender" placeholder="请选择性别">
          <a-select-option value="boy">男</a-select-option>
          <a-select-option value="girl">女</a-select-option>
        </a-select>
      </a-form-item>

      <a-form-item label="需求" name="demand">
        <a-select
          v-model:value="formState.demand"
          placeholder="请选择您的需求"
        >
          <a-select-option value="事业">事业</a-select-option>
          <a-select-option value="爱情">爱情</a-select-option>
          <a-select-option value="健康">健康</a-select-option>
          <a-select-option value="财运">财运</a-select-option>
          <a-select-option value="学业">学业</a-select-option>
          <a-select-option value="其他">其他</a-select-option>
        </a-select>
      </a-form-item>

      <a-form-item>
        <a-button type="primary" html-type="submit" :loading="loading">
          开始占卜
        </a-button>
      </a-form-item>
    </a-form>

    <template v-if="resultData">
      <a-divider />
      <h3>占卜结果</h3>
      <div style="text-align: left;">
        <div v-html="markdownResult"></div>
      </div>
    </template>
  </a-card>
</template>

<script>
import { defineComponent, reactive, ref, computed } from 'vue';
import { message } from 'ant-design-vue';
import axios from 'axios';
import { marked } from 'marked'; // 引入 marked
import { API_BASE_URL } from '../api/config';

export default defineComponent({
  name: 'GuaView',
  setup() {
    const formState = reactive({
      gender: '',
      demand: '',
    });

    const resultData = ref(null);
    const loading = ref(false);

    const markdownResult = computed(() => {
      if (resultData.value) {
        const md = `
### 卦象：${resultData.value.gua}

### 动爻：${resultData.value.dongyao}

### 变卦：${resultData.value.biangua}

### 解读：
${resultData.value.result}
`;
        return marked(md); // 使用 marked 解析 Markdown
      }
      return '';
    });

    const onFinish = async (values) => {
      loading.value = true;
      try {
        // 确保 values 中包含 gender 和 demand 字段
        const payload = {
          gender: values.gender,
          demand: values.demand
        };

        const response = await axios.post(`${API_BASE_URL}/zhanbu`, payload, {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
        });
        console.log(response.data.status)
        if (response.data.status === 'success') {
          resultData.value = response.data;
        } else if (response.data.status === 'limited') {
          // 如果返回 status 为 "limited"，则显示 message 中的内容
          message.warning(response.data.message);
        }
        else {
          message.error('占卜失败，请稍后再试。');
        }
      } catch (error) {
        console.error('占卜请求出错:', error);
        message.error('占卜请求出错，请检查网络连接。');
      } finally {
        loading.value = false;
      }
    };

    return {
      formState,
      resultData,
      loading,
      onFinish,
      markdownResult,
    };
  },
});
</script>

<style scoped>
/* 可以添加一些样式调整，例如卡片宽度等 */
/* 移除 pre 和 code 的样式，交给 marked 处理 */
</style>
