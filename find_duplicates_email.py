# find_duplicates_email.py

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

### --- CONFIGURATION ---

# Spreadsheet to analyze
SPREADSHEET_FILE = "your_spreadsheet.xlsx"  # or "your_file.csv"

# Columns to check for duplicates
DUPLICATE_COLUMNS = ["Column1", "Column2"]

# Email settings
SENDER_EMAIL = "your_email@gmail.com"
RECEIVER_EMAIL = "friend_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"

# SMTP server settings (Gmail example)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

### --- MAIN SCRIPT ---

def find_duplicates():
    print("Loading spreadsheet...")
    df = pd.read_excel(SPREADSHEET_FILE)

    print(f"Checking for duplicates in columns: {DUPLICATE_COLUMNS}")
    duplicates = df[df.duplicated(subset=DUPLICATE_COLUMNS, keep=False)]

    if duplicates.empty:
        print("No duplicates found.")
        return "No duplicates found."
    else:
        print(f"Found {len(duplicates)} duplicate rows.")
        return duplicates.to_string(index=False)

def send_email(body_text):
    print("Preparing email...")
    message = MIMEMultipart()
    message["Subject"] = "Duplicate Report"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    message.attach(MIMEText(body_text, "plain"))

    print("Connecting to email server...")
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())

    print("Email sent successfully!")

if __name__ == "__main__":
    print("----- Duplicate Finder Started -----")
    report_text = find_duplicates()
    send_email(report_text)
    print("----- Duplicate Finder Finished -----")
