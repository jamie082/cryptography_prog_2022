import hashlib
import os
import getopt, sys
import logging
from cryptography.fernet import Fernet, MultiFernet

argumentList = sys.argv[1:]

options = "hmo:"

long_options = ["One", "Two", "Three", "Four"]

message = "some secret message".encode()

key = Fernet.generate_key()
fernet = Fernet(key)

message = "hello"

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

def usage():
    print ("This is the help menu")

def create_token(): # print string key
    key1 = Fernet(Fernet.generate_key())
    key2 = Fernet(Fernet.generate_key())
    f = MultiFernet([key1, key2])
    token = f.encrypt(b"Secret message!")
    print(token)

def decrypt_token():
    key1 = Fernet(Fernet.generate_key())
    key2 = Fernet(Fernet.generate_key())
    f = MultiFernet([key1, key2])
    token = f.decrypt(token)
    print (token)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "one", "two", "three", "four="])

    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"): # display help
            usage()
            sys.exit()
        elif o in ("-md5", "--one"):
            print(compute_md5("file_encrypt.py"))
        elif o in ("-sha256", "--two"):
            print(compute_sha256("file_encrypt.py"))
        elif o in ("-encrypt", "--three"):  # encrypt string
            create_token()
        elif o in ("-decrypt", "--four"):  # decrypt string
            decrypt_token()
        else:
            assert False, "unhandled option"

def compute_md5(file_name):
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()

def compute_sha256(file_name):
    with open(file_name, "rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print(readable_hash)

if __name__ == "__main__":
    main()