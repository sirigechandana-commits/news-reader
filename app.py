from flask import Flask, render_template, request
import main   # importing your existing logic

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
    app.run(debug=True)
