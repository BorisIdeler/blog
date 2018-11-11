from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os

import smtplib
from email.message import EmailMessage

@shared_task
def send_mail(content):
    message = EmailMessage()
    message.set_content(content)

    message['Subject'] = content
    message['From'] = os.environ.get('MAIL_LOGIN')
    message['To'] = os.environ.get('MAIL_DESTINATION')

    smtp = smtplib.SMTP_SSL(os.environ.get('MAIL_SMTP'), os.environ.get('MAIL_PORT'))
    smtp.login(os.environ.get('MAIL_LOGIN'), os.environ.get('MAIL_PASSWORD'))
    smtp.send_message(message)
    smtp.quit()