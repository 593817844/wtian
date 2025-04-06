from fastapi import FastAPI,APIRouter
from pydantic import BaseModel
from utils import logs
app =APIRouter()

logger = logs.getLogger(os.environ.get('APP_NAME'))



# 定义请求体的模型
class BaziRequest(BaseModel):
    date: str  # 格式如 "19980218 06"
    sex: str  # "boy" 或 "girl"
    demand: str  # 如 "问事业"


@app.post("/bazi")
async def bazi(request: BaziRequest):
    # 构造返回数据
    

    response = {
        "status": "success",
        "bazi": bazi_info,
        "analysis": result
    }
    return response