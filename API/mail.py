import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = 'myUsernameLabsMObile'
receiver_email = '12015550123@api.labsmobile.com'
subject = 'myTokenLabsMobile'
message = 'Your verification code is 123'


smtp_server = 'addressSmtp'
smtp_port = 465
username = 'myUsernameEmail'
password = 'myPasswordEmail'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
        smtp.login(username, password)
        smtp.send_message(msg)
        print('Email sent successfully.')

except Exception as e:
    print(f'Error: {e}')
            