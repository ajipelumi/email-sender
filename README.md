# Email Sender

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A simple email sender that sends emails using the Gmail SMTP server.

## Usage

1. Clone the repository
2. All modules required are standard Python libraries, so you don't need to install any dependencies.
3. Run the script using `python email_sender.py` in the root directory of the project.

### Configuration

- You need to create a `config.json` file in the root directory of the project with the following content:

```json
{
    "email_name": "your_name",
    "email_user": "your_email",
    "email_password": "your_email_password"
}
```

Note: Make sure to enable the "Less secure app access" in your Gmail account settings or create an app password if you have 2-step verification enabled.

- The body of the email is read from a file named `email_body.txt` in the root directory of the project.

- The subject of the email is read from a file named `email_subject.txt` in the root directory of the project.

- The recipients of the email are read from a file named `recipients.csv` in the root directory of the project. The CSV file should have a header row with the column name `email_address`. (See `recipients.csv` for an example).

- The attachments are read from the `attachments` directory in the root directory of the project.

## Features

- Send emails to multiple recipients.
- Attach files to the email.
- Read the email body and subject from files.
- Read the recipients from a CSV file.

## Future Improvements

- Add support for other email providers.
- Add support for HTML emails.
- Add support for sending emails at a specific time.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or bug fixes.

## License

Email Sender is licensed under the [MIT License](LICENSE).

## Author

**Ajisafe Oluwapelumi** - Software Engineer & Designer

- [GitHub](https://github.com/ajipelumi)  
- [LinkedIn](https://www.linkedin.com/in/ajisafeoluwapelumi/)  
- [Twitter](https://twitter.com/the_pelumi)  
- [Dev](https://dev.to/ajipelumi)
