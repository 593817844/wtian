export APP_NAME=wtian
export WORKERS=4
export PORT=8000
export DASHSCOPE_API_KEY="xxxxxxxxxxx"
export DB_HOST="127.0.0.1"
export DB_PORT="3306"
export DB_USER="root"
export DB_PASSWORD="123456"
export DB_DATABASE="wtian"
gunicorn -w $WORKERS -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT