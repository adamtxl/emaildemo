# 📩 Find Duplicates and Email Results

This is a simple Python script that looks for **duplicate rows in a spreadsheet** and emails the results.

You can run it any time manually, or later automate it (daily, weekly, etc).

---

## 🚀 How It Works

✅ You provide a **spreadsheet** (Excel or CSV)
✅ It looks for **duplicates** in whatever columns you pick
✅ It **emails you** a report with the results

---

## 🐍 Setup Instructions (for beginners)

You only need Python installed (version 3.9 or newer recommended).
We'll use a “virtual environment” so everything stays nice and clean.

---

### 1️⃣ Clone or download this project

```bash
git clone https://github.com/YOUR_USERNAME/find-duplicates-emailer.git
cd find-duplicates-emailer
```

OR just download the ZIP and unzip it.

---

### 2️⃣ Set up a virtual environment

```bash
# Create the venv (first time)
python3 -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate

# On Windows (Command Prompt):
venv\Scripts\activate
```

---

### 3️⃣ Install required libraries

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configure the script

Open `find_duplicates_email.py` in any text editor.

At the top of the file, you'll see settings like:

```python
SPREADSHEET_FILE = "your_spreadsheet.xlsx"
DUPLICATE_COLUMNS = ["Column1", "Column2"]

SENDER_EMAIL = "your_email@gmail.com"
RECEIVER_EMAIL = "friend_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```

Update these to match:

✅ The **spreadsheet file name**
✅ The **columns to check for duplicates**
✅ Your **email settings**

**IMPORTANT:** If using Gmail, you will need to create an **App Password** (regular password will not work).
[Here’s how to create a Gmail App Password →](https://support.google.com/accounts/answer/185833)

---

## 🏃 How to run the script

```bash
# Activate venv if not already active
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate  # Windows

# Run the script
python find_duplicates_email.py
```

You'll see something like:

```
----- Duplicate Finder Started -----
Loading spreadsheet...
Checking for duplicates in columns: ['Name', 'Email']
Found 3 duplicate rows.
Preparing email...
Connecting to email server...
Email sent successfully!
----- Duplicate Finder Finished -----
```

---

## ⏭️ Future Ideas

✅ Automatically run on a schedule (daily/weekly) with **Task Scheduler** or **cron**
✅ Attach the duplicate rows as an **Excel file**
✅ Move config settings to a separate **config file**

---

## ❤️ Credits

Created by Adam Troxell to help my awesome friend learn Python & automate boring stuff! 🚀

---
