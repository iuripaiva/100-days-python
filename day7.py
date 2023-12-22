# Aprendizados do day 7: 

# Esse dia foi focado majoritariamente no desafio final, aplicando todos os termos aprendidos até então como if e else, loops, funções etc.

# DESAFIO FINAL DO DIA 7:

# HANGMAN - A Forca.
import random, hangman_words, hangman_art

def play_game():

    # SELEÇÃO ALEATORIA DA PALAVRA (IMPORTADA DE OUTRO ARQUIVO COM AS PALAVRAS DISPONÍVEIS)
    chosen_word = random.choice(hangman_words.word_list)

    # CONTADOR DE VIDAS
    lives = 6

    print(hangman_art.logo)

    # print(f"\nDebug: The word is '{chosen_word}'.\n")

    # CRIAÇÃO DO DISPLAY DA PALAVRA VAZIA
    display = []
    total_guesses = ""
    for letter in chosen_word: # PRA CADA LETRA DA PALAVRA...
        display += "_" # FAZ UMA LINHA PRO DISPLAY

    end_of_game = False

    while not end_of_game: # ENQUANTO NÃO FOR O FIM DO JOGO...
        print(hangman_art.stages[lives])
        print(display)

        # INPUT DA LETRA ESCOLHIDA
        guess = input("\nChoose a letter: ").lower()

        # ADICIONAR LOGICA PRA CHECAR A LETRA NA PALAVRA
        for position in range (0, len(chosen_word)): # PRA CADA LETRA NA PALAVRA...
            letter = chosen_word[position] # ARMAZENA A LETRA DA POSIÇÃO NA ITERAÇÃO ATUAL.
            if letter == guess: # SE A LETRA SELECIONADA TIVER NA PALAVRA...
                display[position] = letter # SUBSTITUI NO DISPLAY, NA MESMA POSIÇÃO QUE A PALAVRA.
                print(f"\nWrong guesses: {total_guesses}")
                print("")
                if "_" not in display: # SE NÃO TIVEREM MAIS ESPAÇOS VAZIOS...
                    end_of_game = True # FIM DE JOGO.
                    print(hangman_art.stages[lives])
                    print("")
                    print(''.join(display))
                    print("\nYou win.")
                    play_again = input("\nWant to play again (y / n)? ").lower()
                    if play_again == "y":
                        play_game()
                    else:
                        print("\nOk, see ya! :)")
        if guess not in chosen_word:
            lives -= 1
            total_guesses += guess + " "
            print(f"\nWrong guesses: {total_guesses}")
            print("")
            if lives == 0: # SE AS VIDAS ACABAREM E A FORCA FOR PREENCHIDA...
                end_of_game = True # FIM DE JOGO.
                print(hangman_art.stages[lives])
                print("")
                print(display)
                print("\nYou lose.")
                print(f"\nThe answer was {chosen_word}.")
                play_again = input("\nWant to play again (y / n)? ").lower()
                if play_again == "y":
                    play_game()
                else:
                    print("\nOk, see ya! :)")

play_game()