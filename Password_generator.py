# Welcome the user
# Ask the amounts of passwords the user wants
# Ask for users password preferred length
# Print the passwords
# If initial response is no , exit the program

import random

print ("Welcome to your Password Generator")

chars = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM1234567890!@£$%^&*_+:?")
number = input("Amounts of password to Generate: ")
number = int(number)

length = input("Input your password Length: ")
length = int(length)

print("\n Here are your passwords: ")
for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
    

