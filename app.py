from datetime import datetime
from flask import Flask, render_template, request

from mailer import notify_owner


# ── APP ──────────────────────────────────────────────────
app = Flask(__name__)


# ── ROUTES ───────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    data = request.form.to_dict()
    data["ts"] = datetime.now().isoformat()

    notify_owner(data)

    return render_template("index.html", success=True)