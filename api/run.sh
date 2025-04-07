export APP_NAME=wtian
export WORKERS=4
export PORT=8000
export DASHSCOPE_API_KEY="xxxxxxxxxxx"
gunicorn -w $WORKERS -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT