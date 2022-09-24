from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app= Flask(__name__)
@app.route('/',methods =["GET","POST"])
def index():
    url = "https://indiatechnologynews.in/technology/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    # print(soup.prettify())
    outerdata = soup.find_all("div", class_="post__text-inner", limit=10)
    finalNews = ""
    for data in outerdata:
        news = data.h3.a.next_element
        finalNews += "\u2022 " + news + "\n"
    return render_template("index.html", News=finalNews)



