import smtplib
from email.message import EmailMessage
from secrets import sender_email,receiver_email,password

#email details
def send_email(reciever_email:str, subject:str, content:str)->str:
    """Send an email to the specified recipient"""
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = reciever_email
    msg["Subject"] = subject
    msg.set_content(content)

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

    print("Email sent successfully!")

