import hashlib
import os
import getopt, sys
from cryptography.fernet import Fernet

argumentList = sys.argv[1:]

options = "hmo:"

long_options = ["One", "Two", "Three", "Four", "=Five"]

file_name = input("Enter file to search for: ")


try:
    # parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--help"):
            print ("Displaying Help", print(compute_md5(file_name)))

        elif currentArgument in ("-md5", "--two"):
            print ("Output md5", print(compute_md5(file_name)))

        elif currentArgument in ("-sha256", "--three"):
            print ("Displaying file_name:", print(compute_sha256(file_name)))

        elif currentArgument in ("-encrypt", "--four"):
            print ("Encrypt file", write_key())

        elif currentArgument in ("-decrypt", "--five"):
            print ("Decrypt file", read_key())

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

def write_key():

    """ Generate Key and save it into a file
    """

    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():

    """ Load the key from the current directory named 'key.key'
    """
    return open("key.key", "rb").read()