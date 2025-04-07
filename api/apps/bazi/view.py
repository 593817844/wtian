from fastapi import APIRouter
from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from datetime import datetime
from utils import logs
import os
from .bazi import calculate_bazi
app =APIRouter()

logger = logs.getLogger(os.environ.get('APP_NAME'))



# 定义请求体的模型
class BaziRequest(BaseModel):
    birth: str  # 格式如 "19980218 06"
    gender: str  # "boy" 或 "girl"
    demand: str  # 如 "问事业"


# 读取提示词文件的异步函数
async def read_prompt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

@app.post("/bazi")
async def bazi(request: BaziRequest):
    # 构造返回数据
    bazi = await calculate_bazi(request.birth)

    # 设置 API 的 base_url
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

    # 创建 ChatOpenAI 实例，用于调用 Qwen Max
    chat = ChatOpenAI(
        model="qwen-max",  # 使用 Qwen Max 模型
        openai_api_key=os.environ["DASHSCOPE_API_KEY"],  # 从环境变量获取 API Key
        openai_api_base=base_url,  # 设置 base_url
    )

    # 从文件读取提示词模板
    template = await read_prompt("prompts/base.txt")

    # 创建 PromptTemplate
    prompt = PromptTemplate(
        input_variables=["gender", "bazi", "shishen", "wuxing", "demand", "today"],
        template=template
    )

    # 填充模板
    input_prompt = prompt.format(
        gender=request.gender,
        bazi=bazi["bazi"],
        shishen=bazi["shishen"],
        wuxing=bazi["wuxing"],
        demand=request.demand,
        today=datetime.now()
    )

    # 定义消息
    messages = [
        HumanMessage(content=input_prompt),  # 使用填充后的提示词
    ]

    # 调用模型
    response = await chat.ainvoke(messages)

    # 打印响应内容（可选，用于调试）
    print(response.content)

    
    return {
        "status": "success",
        "gender": request.gender,
        "bazi": bazi["bazi"],
        "shishen": bazi["shishen"],
        "wuxing": bazi["wuxing"],
        "result": response.content
    }