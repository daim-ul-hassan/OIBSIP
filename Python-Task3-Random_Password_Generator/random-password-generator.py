import random
import string

print("""
========================================
     RANDOM PASSWORD GENERATOR
========================================

Welcome! Let's generate a strong random password.

Rules:
1. Password length must be at least 8 characters.
2. Choose at least 2 character types.
3. Character types can include uppercase letters,
   lowercase letters, numbers and symbols.
4. Enter y for Yes or n for No when selecting options.
5. You can generate another password without
   restarting the program.

Let's get started!
""")

try:
    password_length = int(input("Enter password length: "))

    if password_length >= 8:
        print("Valid password length.")

        uppercase = input("Include uppercase letters? (y/n): ").lower()
        
        while uppercase != "y" and uppercase != "n":
                print("Invalid input. Please enter y or n.")
                uppercase = input("include uppercase letters? (y/n): ").lower()

        lowercase = input("Include lowercase letters? (y/n): ").lower()

        while lowercase != "y" and lowercase != "n":
                print("Invalid input.Please enter y or n.")
                lowercase = input("Include lowercase letters? (y/n): ").lower()

        numbers = input("Include numbers? (y/n): ").lower()

        while numbers != "y" and numbers != "n":
                print("Invalid input.Please enter y or n.")
                numbers = input("Include numbers? (y/n): ").lower()

        symbols = input("Include symbols (y/n): ").lower()

        while symbols != "y" and symbols != "n":
                print("Invalid input.Please enter y or n.")
                symbols = input("Include symbols? (y/n): ").lower()

        selected_types = 0

        if uppercase == "y":
            selected_types += 1
        if lowercase == "y":
            selected_types += 1
        if numbers == "y":
            selected_types += 1
        if symbols == "y":
            selected_types += 1 
    
        if selected_types < 2:
            print("Error : Please select at least 2 character types.")
        else:
            character_pool = ""

            if uppercase == "y":
                character_pool += string.ascii_uppercase
            if lowercase == "y":
                character_pool += string.ascii_lowercase
            if numbers == "y":
                character_pool += string.digits
            if symbols == "y":
                character_pool += string.punctuation

            print("Character types selected:", selected_types)
            print("Character pool created.")

            while True:
                password = ""

                for i in range(password_length):
                    password += random.choice(character_pool)

                print("Your password: ",password)

                again = input("Generate another password? (y/n): ").lower()

                while again != "y" and again != "n":
                    print("Invalid input.Please enter y or n.")
                    again = input("Generate another password? (y/n): ").lower()

                if again == "n":
                    break

    else:
        print("your password length is smaller than 8.")

except ValueError:
    print("Error : Please enter a valid number.")