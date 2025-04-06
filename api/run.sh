export APP_NAME=wtian
WORKERS=4
export PORT=8000
gunicorn -w $WORKERS -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT