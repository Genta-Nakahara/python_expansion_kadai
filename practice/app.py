import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    with urlopen("https://b.hatena.ne.jp/hotentry/all") as res:
        html = res.read().decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")
    items = soup.select(".entrylist-contents-title a")
    shuffle(items)
    item = items[0]
    print(item)
    return json.dumps({
        "content" : item["title"],
        "link": item["href"]
    })

if __name__ == "__main__":
    app.run(debug=True, port=5004)
