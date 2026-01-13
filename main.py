import requests
from datetime import date, timedelta
import pyttsx3

API_KEY = "0d08606a2b3f42fa8bf101358a452cf7"
BASE_URL = "https://newsapi.org/v2/everything"


def get_news(days, topic):
    from_date = date.today() - timedelta(days=days)

    params = {
        "q": topic,
        "from": from_date,
        "sortBy": "publishedAt",
        "apiKey": API_KEY,
        "language": "en",
        "pageSize": 5
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # ✅ DEFINE articles HERE
    articles = data.get("articles", [])

    headlines = []

    for article in articles:
        if article["title"]:
            headlines.append(article["title"])

    # 🔊 create audio
    if headlines:
        engine = pyttsx3.init()
        text = ". ".join(headlines)
        engine.save_to_file(text, "static/news_audio.wav")
        engine.runAndWait()

    return headlines
