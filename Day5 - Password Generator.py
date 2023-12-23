# Termos aprendidos durante o day 5: 

# Loops:

# for loop:
#   fruits = ["Apple", "Peach", "Pear"]
#   for fruit in fruits:
#       print(fruit)

# for ... in range:
#   total = 0
#   for number in range (0, 100):
#       total += number
#   print(total)

# DICA: O numero final do range não conta com ele mesmo, ex: Se usar um range de 1 a 100, só vai contar do 1 até o 99. O melhor nesse caso é fazer de 0 a 100 ou de 1 a 101.

# DESAFIO FINAL DO DIA 5:

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!")

nr_letters = int(input("\nHow many letters would you like in your password: "))
nr_symbols = int(input("\nHow many symbols would you like in your password: "))
nr_numbers = int(input("\nHow many numbers would you like in your password: "))

password = ""

for letter in range (0, nr_letters):
    password += random.choice(letters) # .choice() é uma função da biblioteca random que retorna um elemento escolhido aleatoriamente de uma determinada sequencia, como a lista "letters" nesse caso.

for symbol in range (0, nr_symbols):
    password += random.choice(symbols)

for number in range (0, nr_numbers):
    password += random.choice(numbers)

password_list = list(password) # Cria uma lista, separando cada caractere da variavel "password" em indices e armazena na variavel "password_list"

random.shuffle(password_list) # Usa a função .shuffle() pra embaralhar a lista armazenada na variavel "password_list"

password = ''.join(password_list) # Junta toda a lista em uma string só e sobrescreve a variavel "password" inicial

print(f"\nHere is your password: {password}\n")
