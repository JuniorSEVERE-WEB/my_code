import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "Mon premier email depuis Python"
msg['From'] = "ton_email@gmail.com"
msg['To'] = "destinataire@example.com"
msg.set_content("Bonjour, ceci est un test !")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("ton_email@gmail.com", "ton_mot_de_passe")
    smtp.send_message(msg)
    print("Email envoyé !")