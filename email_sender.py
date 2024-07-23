import logging
from email_sender_app.email_helpers import (
    load_email_config, read_recipients_from_csv, read_email_subject,
    read_email_body, read_attachments_from_directory, send_email
)

# Set up logging to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("email_log.txt"),
        logging.StreamHandler()
    ]
)


def main():
    config = load_email_config()
    recipient_emails = read_recipients_from_csv()
    subject = read_email_subject()
    body = read_email_body()

    sender_name = config['email_name']
    sender_email = config['email_user']
    sender_password = config['email_password']
    attachments = read_attachments_from_directory()

    send_email(subject, body, sender_name, sender_email, sender_password, recipient_emails, attachments=attachments)


if __name__ == "__main__":
    main()
