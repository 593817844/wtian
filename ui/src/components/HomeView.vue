<template>
  <a-card class="w-full max-w-2xl mx-auto" hoverable>
    <template #title>
      <h2 class="text-2xl font-semibold text-gray-700">欢迎体验易经算命</h2>
    </template>
    <div class="prose text-gray-600">
      <p>欢迎来到易经算命平台！我们提供专业的命理分析和占卜服务，帮助您探索人生运势与未来方向。</p>
      <h4 class="text-lg font-semibold mt-4">功能介绍</h4>
      <ul>
        <li><strong>八字测算</strong>：输入出生日期和性别，获取详细的八字排盘和命盘分析，了解五行平衡与运势建议。</li>
        <li><strong>64卦占卜</strong>：通过易经64卦占卜，解答您的问题或提供随机指引，洞悉未来趋势。</li>
      </ul>
      <p>点击顶部导航栏，开始您的命理之旅！</p>
    </div>
  </a-card>
</template>

<script>
export default {
  name: 'HomeView'
};
</script>

<style scoped>
/* You can add custom styles here if needed, or override existing ones */
.ant-card-head {
  border-bottom: 1px solid #f0f0f0; /* Add a subtle border to the card header */
}

.ant-card-body {
  padding: 24px; /* Add some padding to the card body */
}

.prose {
  line-height: 1.75;
}

.prose ul {
  list-style-type: disc;
  padding-left: 2rem;
}

.prose li {
  margin-bottom: 0.5rem;
}

.prose strong {
  font-weight: 600;
}
</style>
