import os
from fastapi import FastAPI
from utils import middleware,exceptions
from fastapi.middleware.cors import CORSMiddleware
from apps.bazi.view import app as bazi_app
from apps.zhanbu.view import app as zhanbu_app

def create_app() -> FastAPI:
    """工厂函数：创建App对象"""
    # 读取环境配置文件的信息，加载到环境变量
    app = FastAPI(
        title="Twen",
        # 注册全局异常处理函数
        exception_handlers={
            exceptions.HTTPException: exceptions.global_http_exception_handler,
            exceptions.RequestValidationError: exceptions.global_request_exception_handler,
        }
    )

    # 允许跨域的来源，可以设置为前端的 URL 地址
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 这里设置为前端地址，如果前端是用 React/Vue 的开发服务器，通常是 http://localhost:3000
        allow_credentials=True,
        allow_methods=["*"],  # 允许所有 HTTP 方法
        allow_headers=["*"],  # 允许所有请求头
    )

    # 注册路由
    app.include_router(bazi_app)
    app.include_router(zhanbu_app)
    
    # 注册中间件函数
    http_middleware = app.middleware('http')
    http_middleware(middleware.log_requests)

    return app

app = create_app()
