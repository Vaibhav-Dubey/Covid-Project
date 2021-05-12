import smtplib, ssl
def sendemail():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "coviddocs2021@gmail.com"  # Enter your address
    receiver_email = "vaibhavdubey1999@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
