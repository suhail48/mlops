import smtplib

#import config


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('9634085841suh@gmail.com', '9756482639suhai.')
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('9634085841suh@gmail.com', '9634085841suh@gmail.com', message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "MLOPS"
msg = "Hello there, your Deep Learning model has more than 95% efficiency."

send_email(subject, msg)