from flask import Flask, render_template, request, redirect
import logging, json
from datetime import datetime

app = Flask(__name__)
#logging.basicConfig(filename='logs.txt', level=logging.INFO)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    data = request.form.to_dict()
    data["ts"] = datetime.now().isoformat()
    #logging.info(json.dumps(data, ensure_ascii=False))
    return render_template("index.html", success=True)