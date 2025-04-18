from fastapi import APIRouter,Depends
from utils.access_limit import check_ip_access

from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from datetime import datetime
from utils import logs
from .bazi import calculate_bazi
from utils.commom import logger,read_prompt,chat
from .scheams import PaipanRequest,PaipanResponse,FenxiRequest

app =APIRouter()


@app.post("/bazi/paipan",response_model=PaipanResponse)
async def paipan(request: PaipanRequest):
    # 构造返回数据
    bazi = calculate_bazi(request.birth)
    resp = {
        "gender": request.gender,
        "old_birth": bazi["nong_time"],
        "bazi": bazi["bazi"],
        "shishen": bazi["shishen"],
        "wuxing": bazi["wuxing"]
    }
    return resp

@app.post("/bazi/fenxi")
async def bazifenxi(request: FenxiRequest,ip_check=Depends(check_ip_access)):
    print(ip_check)
    if ip_check["status"] == "limited":
        return ip_check
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
        bazi=request.bazi,
        shishen=request.shishen,
        wuxing=request.wuxing,
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
        "result": response.content
    }