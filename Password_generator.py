# Ask the user if they want to generate the password or not
# If yes , ask for the password length
# Generate the password d
# Print the password 
# If initial response is no , exit the program


import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

#Create a function

def generate_password():
        password_length = int(input("How long would you like your password to be? "))

        random.shuffle(characters)

        password = []

        for x in range(password_length):
            password.append(random.choice(characters))
        random.shuffle(password)

        password = "".json(password)

        print(password)

        option = input("Do you want to generate the password? (Yes / No): ")
        if option == "Yes":
            generate_password()
        elif option == "No":
            print("Program ended")
            quit()
        else:
            print("Invalid input, Please input Yes or No")
        quit()

    


        

