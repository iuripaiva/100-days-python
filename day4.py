# Termos aprendidos durante o day 4: 

# Aleatorização: Uso da biblioteca random (random.randint() e random.random()).
    # random.randint(a, b): Gera um número aleatório dentro do intervalo de a até b, e inclui os dois valores também.
    # random.random(): Gera um numero de ponto flutuante (float) no intervalo de 0.0 a 0.1, mas não inclui o 1.0.

# Importação e exportação de códigos: Usando import de outro arquivo criado anteriormente e também importando a biblioteca random.

# Python Lists: 
    # Regular Lists:
        # Exemplo de lista: fruits = ["Apple", "Banana", "Orange"]
        # Exemplo de consulta a essa lista: print(fruits[1]) ==> O resultado será Banana.
        # DICA: Listas iniciam a contagem a partir do 0, assim como praticamente tudo na programação. Porém, se você buscar algo numa lista iniciando por -1, ela será contada de trás pra frente.
            # DICA ex: print(fruits[-1]) ==> O resultado será Orange.
        # DICA2: Pra mudar um valor dentro de uma lista, basta selecionar o index dela e alterar o valor
            # DICA2 ex: fruits[2] = "Cherry" ==> Isso vai substituir a fruta no index 2 (Orange) por Cherry.
        # DICA3: Pra adicionar um novo dado na lista, usa-se a função "append()".
            # DICA3 ex: fruits.append("Pear") ==> Vai adicionar uma nova posição no final da lista, com o valor "Pear".
    # Nested Lists:
        # Exemplo de nested list: food = [["apple", "strawberry", "banana", "pear"],["lettuce", "cabbage", "broccoli", "spinach"]]
            # Na lista acima existem 2 listas dentro de uma principal, separando as comidas por frutas e verduras.

    # DICA MASTER: NÃO memorize todas as funções da lista ou algo do tipo, você só precisa saber o que precisa e buscar na documentação pra implementar. CONSULTE, não MEMORIZE.


# DESAFIO FINAL DO DIA 4:

import random as r

rock = """
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_img = [rock, paper, scissors]

print("Welcome to the Rock, Paper, Scissors game!\n")

computer_choice = r.randint(0,2)
player_choice = int(input("Choose 0 for rock, 1 for paper or 2 for scissors: "))

# INVALID NUMBER
if player_choice < 3 and player_choice > -1: # OPTIONS ONLY GO FROM 0 TO 2

    print(f"\nYou chose:")
    print(game_img[player_choice])

    print(f"The computer chose:")
    print(game_img[computer_choice])

    # WINS AND LOSSES
    if player_choice == 0 and computer_choice == 2: # ROCK (0) BEATS SCISSORS (2)
        print("You win.")
    elif computer_choice == 0 and player_choice == 2: # ROCK (0) BEATS SCISSORS (2)
        print("You lose.")
    elif player_choice < computer_choice:  # THE SMALLER NUMBER ALWAYS LOSES (EXCEPT ABOVE CONDITIONS)
        print("You lose.")
    elif player_choice > computer_choice: # THE BIGGER NUMBER ALWAYS WINS (EXCEPT ABOVE CONDITIONS)
        print("You win.")
    # DRAW
    elif player_choice == computer_choice:
        print("It's a draw.")

else:
    print("Invalid number.")