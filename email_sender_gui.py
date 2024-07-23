import tkinter as tk
import os
from tkinter import filedialog, font
from email_sender_app.email_helpers import send_email


class EmailSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Sender App")

        # Set the default font
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Times New Roman")


        # Create the GUI elements
        tk.Label(root, text="Sender Name:").grid(row=0, column=0, padx=10, pady=5)
        self.sender_name_entry = tk.Entry(root, width=50)
        self.sender_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Sender Email:").grid(row=1, column=0, padx=10, pady=5)
        self.sender_email_entry = tk.Entry(root, width=50)
        self.sender_email_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Sender Password:").grid(row=2, column=0, padx=10, pady=5)
        self.sender_password_entry = tk.Entry(root, show='*', width=50)
        self.sender_password_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Email Subject:").grid(row=3, column=0, padx=10, pady=5)
        self.subject_entry = tk.Entry(root, width=50)
        self.subject_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Email Body:").grid(row=4, column=0, padx=10, pady=5)
        self.body_entry = tk.Text(root, width=50, height=10)
        self.body_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Recipient Emails (comma-separated):").grid(row=5, column=0, padx=10, pady=5)
        self.recipient_emails_entry = tk.Entry(root, width=50)
        self.recipient_emails_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Button(root, text="Add Attachments", command=self.add_attachments).grid(row=6, column=0, padx=10, pady=5)
        self.attachments_list = tk.Listbox(root, width=50, height=5)
        self.attachments_list.grid(row=6, column=1, padx=10, pady=5)

        tk.Button(root, text="Send Email", command=self.send_email).grid(row=7, column=0, columnspan=2, pady=10)
        self.status_label = tk.Label(root, text="", fg="red")
        self.status_label.grid(row=8, column=0, columnspan=2)

    def add_attachments(self):
        files = filedialog.askopenfilenames(title="Select Attachments")
        for file in files:
            file_name = os.path.basename(file)
            self.attachments_list.insert(tk.END, file_name)

    def send_email(self):
        sender_name = self.sender_name_entry.get()
        sender_email = self.sender_email_entry.get()
        sender_password = self.sender_password_entry.get()
        subject = self.subject_entry.get()
        body = self.body_entry.get("1.0", tk.END).strip()
        recipient_emails = self.recipient_emails_entry.get().split(',')
        attachments = list(self.attachments_list.get(0, tk.END))

        try:
            send_email(sender_name, sender_email, sender_password, subject, body, recipient_emails, attachments)
            self.status_label.config(text="Email sent successfully!", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Failed to send email: {e}", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailSenderApp(root)
    root.mainloop()
