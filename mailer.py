import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def notify_owner(data: dict):
    msg = EmailMessage()

    msg["Subject"] = f"Nouveau contact : {data.get('objet', 'Sans objet')}"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("OWNER_EMAIL")

    # Permet de répondre directement au visiteur
    if data.get("email"):
        msg["Reply-To"] = data["email"]

    content = f"""
Nouveau message reçu

Nom : {data.get('nom')}
Prénom : {data.get('prenom')}
Email : {data.get('email')}
Téléphone : {data.get('telephone')}
Objet : {data.get('objet')}

Message :
{data.get('message')}
"""

    msg.set_content(content)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        print('couoc')
        smtp.login(
            os.getenv("EMAIL_USER"), #type : ignore # type: ignore
            os.getenv("EMAIL_PASS")  # type: ignore
        )

        smtp.send_message(msg)