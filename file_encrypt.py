import hashlib
import os
import getopt, sys
from cryptography.fernet import Fernet

argumentList = sys.argv[1:]

options = "hmo:"

long_options = ["One", "Two", "Three", "Four", "Five"]

message = "some secret message".encode()

#https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["one", "two", "three", "four="])

    except getopt.GetoptError as err:
        print(err)
        sys.exit()
    output = None
    verbose = False
    for o, a in opts:
        if o == "-h": # display help
            verbose = True
        elif o in ("-md5", "--one"):
            print(compute_md5("file_encrypt.py"))
        elif o in ("-sha256", "--two"):
            print(compute_sha256("file_encrypt.py"))
        elif o in ("-encrypt", "--three"):
            encrypt()
        elif o in ("-decrypt", "--four"):
            decrypt()
        else:
            assert False, "unhandled option"

def find_files(filename, search_path):
    result = []

    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return result.append(root, file_name)
        return result

print(find_files("README.md", "C:\\"))

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


def encrypt():
    
    f = Fernet(key)

    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    print(mykey)

    with open('grades.csv', 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open ('enc_grades.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
def decrypt ():
    with open('enc_grades.csv', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open('dec_grades.csv', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

if __name__ == "__main__":
    main()
