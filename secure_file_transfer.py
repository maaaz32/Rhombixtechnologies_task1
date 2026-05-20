#!/usr/bin/env python3
"""
Secure File Transfer Application
Rhombix Technologies - Cyber Security Internship Task 2
Features: AES Encryption, Access Control, Audit Logs
"""

import os
import hashlib
import logging
from datetime import datetime
from cryptography.fernet import Fernet


# ─────────────────────────────────────────────
#  SETUP AUDIT LOG
# ─────────────────────────────────────────────
logging.basicConfig(
    filename="audit_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log(message):
    """Write a message to the audit log and print it."""
    logging.info(message)
    print(f"[LOG] {message}")


# ─────────────────────────────────────────────
#  ACCESS CONTROL (Simple Username + Password)
# ─────────────────────────────────────────────

# Stored users: username -> hashed password
USERS = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "user1": hashlib.sha256("pass123".encode()).hexdigest(),
}

def login():
    """Ask user to log in. Returns username if successful."""
    print("\n" + "=" * 50)
    print("     Secure File Transfer - Rhombix Technologies")
    print("=" * 50)
    print("\n[!] Please login to continue.\n")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    hashed = hashlib.sha256(password.encode()).hexdigest()

    if username in USERS and USERS[username] == hashed:
        log(f"LOGIN SUCCESS - User: {username}")
        print(f"\n[✓] Welcome, {username}!\n")
        return username
    else:
        log(f"LOGIN FAILED - User: {username}")
        print("\n[✗] Invalid username or password. Access denied.")
        exit()


# ─────────────────────────────────────────────
#  AES ENCRYPTION (via Fernet - AES-128 CBC)
# ─────────────────────────────────────────────

KEY_FILE = "secret.key"

def generate_key():
    """Generate and save an AES encryption key."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    log("Encryption key generated and saved to secret.key")
    return key

def load_key():
    """Load the existing AES key or generate a new one."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        return generate_key()


# ─────────────────────────────────────────────
#  ENCRYPT FILE
# ─────────────────────────────────────────────

def encrypt_file(filepath, username):
    """Encrypt a file using AES and save it as .encrypted"""
    if not os.path.exists(filepath):
        print(f"[✗] File not found: {filepath}")
        log(f"ENCRYPT FAILED - File not found: {filepath} - User: {username}")
        return

    key = load_key()
    fernet = Fernet(key)

    with open(filepath, "rb") as f:
        original = f.read()

    encrypted = fernet.encrypt(original)

    encrypted_path = filepath + ".encrypted"
    with open(encrypted_path, "wb") as f:
        f.write(encrypted)

    print(f"\n[✓] File encrypted successfully!")
    print(f"    Saved as: {encrypted_path}")
    log(f"ENCRYPT SUCCESS - File: {filepath} -> {encrypted_path} - User: {username}")


# ─────────────────────────────────────────────
#  DECRYPT FILE
# ─────────────────────────────────────────────

def decrypt_file(filepath, username):
    """Decrypt an AES encrypted file and restore the original."""
    if not os.path.exists(filepath):
        print(f"[✗] File not found: {filepath}")
        log(f"DECRYPT FAILED - File not found: {filepath} - User: {username}")
        return

    key = load_key()
    fernet = Fernet(key)

    with open(filepath, "rb") as f:
        encrypted = f.read()

    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception:
        print("[✗] Decryption failed! Wrong key or corrupted file.")
        log(f"DECRYPT FAILED - Wrong key or corrupted file: {filepath} - User: {username}")
        return

    decrypted_path = filepath.replace(".encrypted", ".decrypted")
    with open(decrypted_path, "wb") as f:
        f.write(decrypted)

    print(f"\n[✓] File decrypted successfully!")
    print(f"    Saved as: {decrypted_path}")
    log(f"DECRYPT SUCCESS - File: {filepath} -> {decrypted_path} - User: {username}")


# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────

def menu(username):
    """Show the main menu."""
    while True:
        print("\n" + "-" * 40)
        print("  MENU")
        print("-" * 40)
        print("  1. Encrypt a file")
        print("  2. Decrypt a file")
        print("  3. View Audit Log")
        print("  4. Exit")
        print("-" * 40)

        choice = input("Select option (1-4): ").strip()

        if choice == "1":
            path = input("Enter file path to encrypt: ").strip()
            encrypt_file(path, username)

        elif choice == "2":
            path = input("Enter file path to decrypt: ").strip()
            decrypt_file(path, username)

        elif choice == "3":
            print("\n--- AUDIT LOG ---")
            if os.path.exists("audit_log.txt"):
                with open("audit_log.txt", "r") as f:
                    print(f.read())
            else:
                print("No logs found.")

        elif choice == "4":
            log(f"LOGOUT - User: {username}")
            print("\n[✓] Goodbye! Stay secure.")
            break

        else:
            print("[✗] Invalid option. Please choose 1-4.")


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    user = login()
    menu(user)
