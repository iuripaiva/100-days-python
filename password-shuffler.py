import random

print("\nWelcome to Password Shuffler!")
characters = input("\nWrite the password you want to shuffle: ")

password_list = list(characters)

random.shuffle(password_list)

password = ''.join(password_list)

print(f"\nYour new password is: {password}")