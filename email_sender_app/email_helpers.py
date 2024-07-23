import csv
import json
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
import logging
import time
from smtplib import SMTPServerDisconnected, SMTPSenderRefused, SMTPRecipientsRefused, SMTPDataError, SMTPConnectError, SMTPHeloError

def load_email_config(filename='config.json'):
    with open(filename, 'r') as f:
        config = json.load(f)
    return config

def read_recipients_from_csv(filename='recipients.csv'):
    recipient_emails = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['email_address']:
                recipient_emails.append(row['email_address'])
    return recipient_emails

def read_email_subject(filename='email_subject.txt'):
    with open(filename, 'r') as file:
        subject = file.read().strip()
    return subject

def read_email_body(filename='email_body.txt'):
    with open(filename, 'r') as file:
        body = file.read()
    return body

def read_attachments_from_directory(directory='attachments'):
    attachments = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            attachments.append(filepath)
    return attachments

def attach_file(filepath, msg):
    with open(filepath, 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(filepath)}')
    msg.attach(part)

def send_email(subject, body, sender_name, sender_email, sender_password, recipient_emails, smtp_server='smtp.gmail.com', smtp_port=465, retries=3, delay=5, attachments=None):
    msg = MIMEMultipart()
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = ", ".join(recipient_emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if attachments:
        for attachment in attachments:
            attach_file(attachment, msg)

    attempt = 0
    while attempt < retries:
        try:
            if smtp_port == 465:
                server = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=20)
            else:
                server = smtplib.SMTP(smtp_server, smtp_port, timeout=20)
                server.starttls()

            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, msg.as_string())
            server.quit()
            logging.info("Email sent successfully!")
            break
        except (SMTPServerDisconnected, SMTPSenderRefused, SMTPRecipientsRefused, SMTPDataError, SMTPConnectError, SMTPHeloError) as e:
            logging.error(f"Failed to send email: {e}")
            attempt += 1
            if attempt < retries:
                logging.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logging.error("Max retries reached. Could not send email.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            break
