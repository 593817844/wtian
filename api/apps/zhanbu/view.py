from fastapi import APIRouter
from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from datetime import datetime
import os
from utils.commom import logger,read_prompt,chat
from .zhanbu import generate_hexagram

app =APIRouter()



# 定义请求体的模型
class ZhanbuRequest(BaseModel):
    gender: str  # "boy" 或 "girl"
    demand: str  # 如 "问事业"
    


@app.post("/zhanbu")
async def zhanbu(request: ZhanbuRequest):
    zhanbu = generate_hexagram()
    
    # 从文件读取提示词模板
    template = await read_prompt("prompts/zhanbu.txt")

    # 创建 PromptTemplate
    prompt = PromptTemplate(
        input_variables=["gender", "demand", "gua", "ben_xiagua", "ben_shanggua", "donggua","biangua","bian_xiagua","bian_shangua"],
        template=template
    )

    # 填充模板
    input_prompt = prompt.format(
        gender=request.gender,
        demand=request.demand,
        gua=zhanbu["original"]["gua_name"],
        ben_xiagua=zhanbu["original"]["lower"],
        ben_shanggua=zhanbu["original"]["upper"],
        donggua=zhanbu["original"]["moving"],
        biangua=zhanbu["changed"]["gua_name"],
        bian_xiagua=zhanbu["changed"]["lower"],
        bian_shangua=zhanbu["changed"]["upper"]
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
        "demand": request.demand,
        "gua": zhanbu["original"]["gua_name"],
        "donggua": zhanbu["original"]["moving"],
        "biangua":zhanbu["changed"]["gua_name"],
        "result": response.content
    }
    

