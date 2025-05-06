FROM python:3.10

RUN mkdir -p /wtian/api

WORKDIR /wtian/api


COPY . /wtian/api


RUN pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 8000

# 定义启动命令
CMD ["bash", "run-dev.sh"]