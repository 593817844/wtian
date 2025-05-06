from pydantic import BaseModel, constr
from enum import Enum


class Gender(str, Enum):
    boy = "boy"
    girl = "girl"


class PaipanRequest(BaseModel):

    birth: constr(pattern=r'^\d{8}\s[0-2][0-9]$')  # 匹配 "YYYYMMDD HH"
    is_lunar: bool
    gender: Gender


class PaipanResponse(BaseModel):
    gender: str  # "boy" 或 "girl"
    old_birth: str
    new_birth: str  # 公历生日
    bazi: list
    shishen: list
    wuxing: dict

class FenxiRequest(BaseModel):
    gender: Gender  # "boy" 或 "girl"
    bazi: list
    shishen: list
    wuxing: dict
    demand: str