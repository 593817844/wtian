export APP_NAME="wtian"
export WORKERS=4
export PORT=8000
export DASHSCOPE_API_KEY="xxxxxxx"
export RD_HOST="127.0.0.1"
export RD_PORT="16666"
export RD_DB=0
export RD_PASSWORD="123456"
# export WHITELIST_IPS="127.0.0.1"
# export DB_HOST="47.107.237.220"
# export DB_PORT="13333"
# export DB_USER="root"
# export DB_PASSWORD="password"
# export DB_DATABASE="wtian"
gunicorn -w $WORKERS -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT