import smtplib
import time
from getpass import getpass

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


EMAIL_ADDRESS =input("Email address: ")
PASSWORD = getpass("Password: ")
RECEIVER = input("Recevier: ")
print("")
SUBJECT = input("Subject: ")
BODY = input("BODY: ")
FILE_NAME = input("Input attach file name (if don't have any file press ""Enter button""): ")


try:
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECEIVER
    msg['Subject'] = SUBJECT

    msg.attach(MIMEText(BODY,'plain'))

    if len(FILE_NAME) == 0:

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        server.sendmail(EMAIL_ADDRESS, RECEIVER, text)
        server.quit()

    elif len(FILE_NAME) > 0:
        attachment = open(FILE_NAME, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + FILE_NAME)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        server.sendmail(EMAIL_ADDRESS, RECEIVER, text)
        server.quit()




    print("Success: Email sent!")
    time.sleep(5)

except:

    print("Email failed to send.")
    time.sleep(5)