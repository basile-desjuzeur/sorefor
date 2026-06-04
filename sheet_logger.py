import json
import os

import gspread
from dotenv import load_dotenv

load_dotenv()

COLUMNS = ["ts", "nom", "prenom", "email", "telephone", "objet", "message"]


def log_to_sheet(data: dict):
    path = os.getenv("GSHEET_CREDENTIALS_PATH")
    if path:
        gc = gspread.service_account(filename=path)
    else:
        gc = gspread.service_account_from_dict(json.loads(os.getenv("GSHEET_CREDENTIALS")))
    ws = gc.open_by_key(os.getenv("GSHEET_ID")).sheet1
    ws.append_row([data.get(col, "") for col in COLUMNS])
