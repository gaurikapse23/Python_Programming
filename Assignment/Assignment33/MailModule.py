import smtplib
from email.message import EmailMessage

def SendMail(receiver, body, logFile):
    sender = "yourgmail@gmail.com"
    password = "your_app_password"

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = "Platform Surveillance Report"
    msg['From'] = sender
    msg['To'] = receiver

    with open(logFile, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="PlatformLog.log"
        )

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, password)
    server.send_message(msg)
    server.quit()