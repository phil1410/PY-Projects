# PASSWORD CONFIRMATION USING WHILE LOOP
# This program will ask the user to enter a password and confirm it.
# If the passwords match, it will print a success message.# If the passwords do not match, it will ask the user to try again.
# The user will have a limited number of attempts to enter the correct password.

from colorama import Fore # type: ignore
limits = 3
count = 0

while count < limits:
    # print(f'{Fore.BLUE}')
    count += 1
    password = input(Fore.RESET + "Enter your password: ")
    confirmed_password = input("Confirm password: ")

    if password == confirmed_password:
        print(Fore.GREEN + "Password confirmed successfully".upper())
        break
    if count == limits:
        print(Fore.BLUE + "\nYou've reached your limit")
    else:
        print(Fore.RED + "Try again!")

print(Fore.RESET)