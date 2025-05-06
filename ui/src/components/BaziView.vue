<template>
  <a-card class="w-full max-w-2xl mx-auto" hoverable>
    <template #title>
      <h2 class="text-2xl font-semibold text-gray-700">八字排盘</h2>
    </template>
    <a-form :model="baziInput" :label-col="{ span: 6 }" :wrapper-col="{ span: 18 }">
      <!-- 日历类型和出生日期 纵向排列 -->
      <a-row>
        <a-col :span="24">
          <a-form-item label="日历类型" class="form-item-stacked">
            <a-radio-group v-model:value="is_lunar" @change="onCalendarTypeChange">
              <a-radio :value="false">公历</a-radio>
              <a-radio :value="true">农历</a-radio>
            </a-radio-group>
          </a-form-item>
        </a-col>
      </a-row>

      <a-row>
        <a-col :span="24">
          <a-form-item :label="is_lunar ? '出生日期(农历)' : '出生日期(公历)'" class="form-item-stacked">
            <a-date-picker
              v-model:value="birthDate"
              show-time
              format="YYYY-MM-DD HH"
              @change="onBirthDateChange"
              style="width: 30%"
              :locale="locale"
            />
          </a-form-item>
        </a-col>
      </a-row>

      <a-row>
        <a-col :span="24">
          <a-form-item label="性别" class="form-item-stacked">
            <a-select v-model:value="baziInput.gender" placeholder="请选择性别" style="width: 30%">
              <a-select-option value="boy">男</a-select-option>
              <a-select-option value="girl">女</a-select-option>
            </a-select>
          </a-form-item>
        </a-col>
      </a-row>

      <!-- 排盘按钮 居中放置 -->
      <a-form-item :wrapper-col="{ span: 24 }" class="text-center">
        <a-button type="primary" @click="fetchBazi" :loading="loadingBazi">
          排盘
        </a-button>
      </a-form-item>
    </a-form>

    <!-- 八字结果 -->
    <div v-if="baziResult" class="mt-6">
      <h3 class="text-xl font-semibold text-gray-700 mb-4">排盘结果</h3>
      <a-descriptions :column="1" bordered>
        <a-descriptions-item label="公历">{{ baziResult.new_birth }}</a-descriptions-item>
        <a-descriptions-item label="农历">{{ baziResult.old_birth }}</a-descriptions-item>
        <a-descriptions-item label="八字">{{ baziResult.bazi.join(' ') }}</a-descriptions-item>
        <a-descriptions-item label="十神">{{ baziResult.shishen.join(' ') }}</a-descriptions-item>
        <a-descriptions-item label="五行">
          木{{ baziResult.wuxing.木 }}% 火{{ baziResult.wuxing.火 }}% 土{{ baziResult.wuxing.土 }}%
          金{{ baziResult.wuxing.金 }}% 水{{ baziResult.wuxing.水 }}%
        </a-descriptions-item>
      </a-descriptions>
      <div class="text-center">
        <a-button type="primary" @click="fetchFenxi" :loading="loadingFenxi" class="mt-4">
          分析命盘
        </a-button>
      </div>
    </div>

    <!-- 分析结果 -->
    <div v-if="fenxiResult" class="mt-6">
      <h3 class="text-xl font-semibold text-gray-700 mb-4">命盘分析</h3>
      <a-card hoverable>
        <div class="markdown-body" v-html="renderedMarkdown"></div>
      </a-card>
    </div>
  </a-card>
</template>

<script>
import { ref, computed} from 'vue';
import axios from 'axios';
import { message } from 'ant-design-vue';
import moment from 'moment';
import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import zhCN from 'ant-design-vue/es/date-picker/locale/zh_CN'; // Import locale
import MarkdownIt from 'markdown-it'; // Import MarkdownIt
import { API_BASE_URL } from '../api/config';

dayjs.extend(customParseFormat); // 扩展 dayjs 的 customParseFormat 插件
dayjs.locale('zh-cn'); // 设置全局的 dayjs 本地化

export default {
  name: 'BaziView',
  setup() {
    const baziInput = ref({ birth: '', gender: 'boy', is_lunar: false });
    const birthDate = ref(null);
    const baziResult = ref(null);
    const fenxiResult = ref(null);
    const loadingBazi = ref(false);
    const loadingFenxi = ref(false);
    const locale = ref(zhCN); // Set locale
    const is_lunar = ref(false); // 默认使用公历

    const onCalendarTypeChange = (e) => {
      baziInput.value.is_lunar = e.target.value;
    };

    const onBirthDateChange = (date, dateString) => {
      if (dateString) {
        // 使用 dayjs 处理时间，确保正确获取小时
        const formattedDate = dayjs(date);
        const hour = formattedDate.format('HH');
        const datePart = formattedDate.format('YYYYMMDD');
        baziInput.value.birth = `${datePart} ${hour}`;
      } else {
        baziInput.value.birth = '';
      }
    };

    const fetchBazi = async () => {
      loadingBazi.value = true;

      // Validation: Check if birth date and gender are provided
      if (!baziInput.value.birth || !baziInput.value.gender) {
        message.error('请填写完整的出生日期和性别信息！');
        loadingBazi.value = false; // Stop loading
        return; // Exit the function
      }

      console.log('baziInput.value:', baziInput.value); // Inspect the input

      try {
        const response = await axios.post(`${API_BASE_URL}/bazi/paipan`, {
          birth: baziInput.value.birth,
          gender: baziInput.value.gender,
          is_lunar: baziInput.value.is_lunar
        });
        console.log('response.data:', response.data); // Inspect the response

        if (response.data && typeof response.data === 'object') {
          baziResult.value = response.data;
        } else {
          message.error('服务器返回数据格式错误！');
          baziResult.value = null;
        }
        fenxiResult.value = null; // Reset analysis result
      } catch (error) {
        console.error('Error during fetchBazi:', error); // Log the error object
        message.error('排盘失败，请检查输入！');
      } finally {
        loadingBazi.value = false;
      }
    };

    const fetchFenxi = async () => {
      loadingFenxi.value = true;
      try {
        const response = await axios.post(`${API_BASE_URL}/bazi/fenxi`, {
          gender: baziResult.value.gender,
          bazi: baziResult.value.bazi,
          shishen: baziResult.value.shishen,
          wuxing: baziResult.value.wuxing,
          demand: '无',
        });

        if (response.data.status === 'success') {
          fenxiResult.value = response.data;
        } else if (response.data.status === 'limited') {
          // 如果返回 status 为 "limited"，则显示 message 中的内容
          message.warning(response.data.message);
        } else {
          message.error('分析失败！');
        }

      } catch (error) {
        message.error('分析失败！');
      } finally {
        loadingFenxi.value = false;
      }
    };

    const md = new MarkdownIt(); // Create a MarkdownIt instance

    const renderedMarkdown = computed(() => {
      if (fenxiResult.value && fenxiResult.value.result) {
        return md.render(fenxiResult.value.result); // Render the Markdown
      }
      return '';
    });

    return {
      baziInput,
      birthDate,
      baziResult,
      fenxiResult,
      loadingBazi,
      loadingFenxi,
      is_lunar,
      onCalendarTypeChange,
      onBirthDateChange,
      fetchBazi,
      fetchFenxi,
      renderedMarkdown,
      locale,
    };
  },
};
</script>

<style scoped>
/* Use Ant Design Vue's style variables */
/* Example:  Override the primary color */
/* @primary-color: #1890ff; */

/* Improve the hover state on buttons */
.ant-btn-primary {
  &:hover {
    opacity: 0.8; /* Subtle hover effect using opacity */
  }
}

/* Center the button */
.text-center {
  text-align: center;
}

/* Add basic styling for Markdown output */
.markdown-body {
  font-family: sans-serif;
  font-size: 14px;
  color: rgba(0, 0, 0, 0.85);
  text-align: left; /* 左对齐 Markdown 内容 */
}

/* Center form items */
.form-item-center {
  display: flex;
  justify-content: center;
}

.form-item-center .ant-form-item-control {
  width: 100%; /* 确保内容占据可用宽度 */
}

/* Stacked form item layout */
.form-item-stacked .ant-form-item-label {
  text-align: left; /* Align label to the left */
}

.form-item-stacked .ant-form-item-control {
  margin-top: 4px; /* Add some space between label and control */
}
</style>
