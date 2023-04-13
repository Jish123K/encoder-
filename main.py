import os

import logging

import base64

from cryptography.fernet import Fernet

from pyoxidizer import build

def obfuscate_file(filename: str, key: bytes):

    with open(filename, "rb") as f:

        data = f.read()

    f = Fernet(key)

    encrypted_data = f.encrypt(data)

    with open(f"obfuscated_{filename}", "wb") as f:

        f.write(encrypted_data)

    logging.info(f"File obfuscated successfully as 'obfuscated_{filename}'")

def encode_file(filename: str):

    with open(filename, "rb") as f:

        data = f.read()

    obf_data = base64.b64encode(data)

    with open(f"encoded_{filename}", "w") as f:

        f.write("# This file has been encoded using white obfuscate\n\n")

        f.write(f"import base64\nexec(base64.b64decode({repr(obf_data)}))")

    logging.info(f"File encoded successfully as 'encoded_{filename}'")

def main():

    while True:

        print("""

+-------------------------------------------------------------------+

│                                                                   │

│               1. Obfuscate File                                    │

│                                                                   │

│               2. Encode File                                       │

│                                                                   │

│               3. Exit                                              │

│                                                                   │

+-------------------------------------------------------------------+

 """)

        choice = input("Enter your choice: ")

        if choice == "1":

            filename = input("Enter the name of the file to be obfuscated: ")

            key = Fernet.generate_key()

            obfuscate_file(filename, key)

        elif choice == "2":

            filename = input("Enter the name of the file to be encoded: ")

            encode_file(filename)

        elif choice == "3":

            break

        else:

            print("[ERROR!] Invalid input, please try again.")

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    # Build the executable using PyOxidizer

    build()

    # Run the main function

    main()

