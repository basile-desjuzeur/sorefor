import json
import os

import gspread
from dotenv import load_dotenv

load_dotenv()

COLUMNS = ["ts", "nom", "prenom", "email", "telephone", "objet", "message"]


def log_to_sheet(data: dict):
    creds = json.loads(os.getenv("GSHEET_CREDENTIALS"))
    gc = gspread.service_account_from_dict(creds)
    ws = gc.open_by_key(os.getenv("GSHEET_ID")).sheet1
    ws.append_row([data.get(col, "") for col in COLUMNS])
