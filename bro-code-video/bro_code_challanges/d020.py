# encryption program 

# MODULES AND VARIABLES
import random # will help create a new cryptography
import string # just for not write all letters 
chars = list(" " + string.punctuation + string.digits + string.ascii_letters)
key = chars.copy() 
random.shuffle(key) # create a copy of a list and shuffle for make a new encryptation every time you play

# FUNCTIONS:

def cryptography(message):
    print(f"Original message: {message}")
    encrypt=""
    for letter in message:
        index = chars.index(letter)
        encrypt += key[index]
    print(f"Encrypted message:{encrypt}")

def decryption(code):
    decrypt = ""
    for letter in code:
        index = key.index(letter)
        decrypt += chars[index]
    print(f"Decrypted message: {decrypt}")

# PROGRAM:

message = input("Enter a message to encrypt: ")
cryptography(message)
message = input("Enter the message to descrypt:")
decryption(message)
