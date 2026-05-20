import csv
import logging
from datetime import datetime
from flask import Flask, render_template, request

# ── LOGGER ──────────────────────────────────────────────
logger = logging.getLogger("sorefor")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs.txt", encoding="utf-8")
handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
logger.addHandler(handler)

# ── APP ──────────────────────────────────────────────────
app = Flask(__name__)

CSV_FILE = "contacts.csv"
CSV_FIELDS = ["ts", "nom", "prenom", "email", "telephone", "objet", "message"]


def save_to_csv(data: dict) -> None:
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        # Écrit l'entête seulement si le fichier est vide
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(data)


# ── ROUTES ───────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    data = request.form.to_dict()
    data["ts"] = datetime.now().isoformat()

    save_to_csv(data)
    logger.info(f"Nouveau contact : {data['email']} — {data['objet']}")

    return render_template("index.html", success=True)