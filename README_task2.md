# Secure File Transfer Application 🔐

A Python-based secure file transfer application built as part of the **Rhombix Technologies Cyber Security Internship - Task 2**.

## About
This application allows users to securely encrypt and decrypt files using AES encryption. It includes an access control system with hashed passwords and an audit log that records every action performed.

## Features
- AES encryption and decryption of any file
- Login system with username and hashed password protection
- Audit log that records every login, encrypt, and decrypt action with timestamps
- Simple and beginner friendly menu interface

## Technologies Used
- Python 3
- `cryptography` library for AES encryption (Fernet)
- `hashlib` for password hashing
- `logging` for audit logs

## Installation

**Step 1 — Install Python 3**
Download from python.org and install. Make sure to tick "Add Python to PATH"

**Step 2 — Install required library**
```bash
pip install cryptography
```

## How to Run

**Step 1 — Save the file**
Download `secure_file_transfer.py` and save it anywhere on your PC

**Step 2 — Open Command Prompt in that folder**
Hold Shift + Right Click in the folder → Click "Open PowerShell window here"

**Step 3 — Run the program**
```bash
python secure_file_transfer.py
```

**Step 4 — Login**
```
Username: admin
Password: admin123
```

**Step 5 — Encrypt a file**
- Choose option 1
- Type the full path of any file example:
```
D:\test.txt
```

**Step 6 — Decrypt a file**
- Choose option 2
- Type the path of the encrypted file example:
```
D:\test.txt.encrypted
```

**Step 7 — View Audit Log**
- Choose option 3 to see all recorded actions

## Sample Output
```
==================================================
     Secure File Transfer - Rhombix Technologies
==================================================

[!] Please login to continue.

Username: admin
Password: admin123

[✓] Welcome, admin!

----------------------------------------
  MENU
----------------------------------------
  1. Encrypt a file
  2. Decrypt a file
  3. View Audit Log
  4. Exit
----------------------------------------
Select option (1-4): 1
Enter file path to encrypt: D:\test.txt

[✓] File encrypted successfully!
    Saved as: D:\test.txt.encrypted
```

## What I Learned
- How AES encryption works to protect files
- How to hash passwords for secure access control
- How to implement audit logging in Python
- How encryption ensures confidentiality and integrity of files

## Internship
**Company:** Rhombix Technologies
**Domain:** Cyber Security
**Task:** Month 1 - Task 2 (Secure File Transfer Application)
