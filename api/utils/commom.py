from langchain_openai import ChatOpenAI
from utils import logs
import os

logger = logs.getLogger(os.environ.get('APP_NAME'))

base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 创建 ChatOpenAI 实例，用于调用 Qwen Max
chat = ChatOpenAI(
    model="qwen-max",  # 使用 Qwen Max 模型
    openai_api_key=os.environ["DASHSCOPE_API_KEY"],  # 从环境变量获取 API Key
    openai_api_base=base_url,  # 设置 base_url
)

# 读取提示词文件的异步函数
async def read_prompt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()