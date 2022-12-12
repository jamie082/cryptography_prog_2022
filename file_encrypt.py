import hashlib
import os
import getopt, sys
from cryptography.fernet import Fernet

argumentList = sys.argv[1:]

options = "hmo:"

long_options = ["md5", "sha256", "encrypt_file"]

file_name = "file_encrypt.py"
inputFileName = input("Enter search path: ")
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

print(compute_md5(file_name))
print(compute_sha256(file_name))