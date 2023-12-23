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
