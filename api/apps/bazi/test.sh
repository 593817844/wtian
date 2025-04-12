curl -X 'POST' \
  'http://127.0.0.1:8000/bazi/fenxi' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "gender": "boy",
  "bazi": [
    "戊辰",
    "甲寅",
    "戊申",
    "庚申"
  ],
  "shishen": [
    "比肩",
    "七杀",
    "比肩",
    "食神"
  ],
  "wuxing": {
    "木": 25,
    "火": 0,
    "土": 37.5,
    "金": 37.5,
    "水": 0
  },
  "demand": "无"
}'