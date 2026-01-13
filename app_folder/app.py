from flask import Flask, render_template, request
import main
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    news_output = ""

    if request.method == "POST":
        days = int(request.form["days"])
        topic = request.form["topic"]
        news_output = main.get_news(days, topic)

    return render_template("index.html", news=news_output)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
