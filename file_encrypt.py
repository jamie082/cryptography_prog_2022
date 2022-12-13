import hashlib
import os
import getopt, sys
from cryptography.fernet import Fernet

argumentList = sys.argv[1:]

options = "hmo:"

long_options = ["Help", "md5", "sh256", "=decrypt"]

file_name = input("Enter file to search for: ")

try:
    # parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--help"):
            print ("Displaying Help", print(compute_md5(file_name)))

        elif currentArgument in ("-md5", "--two"):
            print ("Output md5", (compute_md5(file_name)))

        elif currentArgument in ("-sha256", "--three"):
            print ("Displaying file_name:", (compute_sha256(file_name)))

        elif currentArgument in ("-encrypt", "--four"):
            print ("Encrypt file")

        elif currentArgument in ("-decrypt", "--five"):
            print ("Decrypt file")

        else:
            exit(0)

except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
def find_files(filename, search_path):
    result = []

    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return result.append(root, file_name)
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
        
print(find_files(file_name, "search_path"))