import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def notify_owner(data: dict):

    for owner in [os.getenv('OWNER_EMAIL_1'), os.getenv('OWNER_EMAIL_2')]:

        msg = EmailMessage()

        msg["Subject"] = f"Nouveau contact : {data.get('objet', 'Sans objet')}"
        msg["From"] = os.getenv("EMAIL_USER")
        msg["To"] = owner

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
            smtp.login(
                os.getenv("EMAIL_USER"), #type : ignore
                os.getenv("EMAIL_PASS") #type : ignore
            )

            smtp.send_message(msg)