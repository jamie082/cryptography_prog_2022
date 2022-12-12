import hashlib
import os
from cryptography.fernet import Fernet

file_name = "file_encrypt.py"
#inputFileName = input("Enter search path: ")
def find_files(filename, search_path):
    result = []

    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, inputFileName)
        return result

def compute_md5(file_name):
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()

def compute_sha256(file_name):
    with open(file_name, "rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        print(readable_hash)

def fernet_compute():
    key = Fernet.generate_key()

    f = Fernet(key=
    token = f.encrypt(b"welcome to geeksforgeeks")

    print(token)

    d = f.decrypt(token)

    print(d)

print(compute_md5(file_name))
fernet_compute()