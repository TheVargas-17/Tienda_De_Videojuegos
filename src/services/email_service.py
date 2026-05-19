import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")


def enviar_correo(destino, asunto, mensaje):

    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = destino
        msg["Subject"] = asunto

        msg.attach(MIMEText(mensaje, "plain"))

        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()

        servidor.login(EMAIL_USER, EMAIL_PASS)

        servidor.send_message(msg)

        servidor.quit()

        return True

    except Exception as e:
        print(e)
        return False