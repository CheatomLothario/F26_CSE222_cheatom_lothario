import json
import os
import hashlib
import secrets

# Location of saved account information
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "accounts.json")

def load_accounts():
    # Checks if account file exists
    if not os.path.exists(DATA_FILE):
        return{}

    # Reads previously saved accounts
    try:
        with open(DATA_FILE, "r") as file:
            accounts = json.load(file)

        if not isinstance(accounts, dict):
            raise ValueError("Invalid account file format.")

        return accounts

    except (OSError, json.JSONDecodeError, ValueError):
        raise ValueError("Unable to read account information.")

def save_accounts(accounts):
    # Saves account information to a JSON file
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)

def hash_password(password, salt):
    # Converts a password to a secure hash
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        600000
    ).hex()

def create_account(username, password):
    # Retrieves existing accounts
    accounts = load_accounts()

    # Checks if username exists
    if username in accounts:
        return False

    # Generates a random salt
    salt = secrets.token_hex(16)

    # Stores username and hashed password
    accounts[username] = {
        "salt": salt,
        "password": hash_password(password, salt)
    }

    # Saves updated account info
    save_accounts(accounts)

    return True
