import arts
from unidecode import unidecode

def start():

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    shifted_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print(arts.caesar_logo)
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    text = text.replace(" ", "") # Remove espaços
    text = unidecode(text) # Remove acentos e caracteres especiais
    shift = int(input("\nType the shift number:\n"))
    
    def caesar(shift_direction,plain_text, shift_amount):
        final_text = ""
        for i in  range (shift_amount):
            shifted_alphabet.append(shifted_alphabet[0]) # Adiciona ao final da lista as letras adicionais pra fazer o shift.
            shifted_alphabet.remove(shifted_alphabet[0]) # Depois remove do início, deixando apenas no final.
        
        for letter in plain_text:
            if shift_direction.lower() == "encode":
                final_text += shifted_alphabet[alphabet.index(letter)] # Adiciona na variavel final_text letra por letra da palavra cifrada.
            elif shift_direction.lower() == "decode":
                final_text += alphabet[shifted_alphabet.index(letter)] # Adiciona na variavel final_text letra por letra da palavra decodificada.
            else:
                print(f"\nYou chose an invalid option. Choose only 'encode' or 'decode'.\n")
                start()
        
        if shift_direction.lower() == "encode":
            print(f"\nThe encoded text is: {final_text}.\n")
        elif shift_direction.lower() == "decode":
            print(f"\nThe decoded text is: {final_text}.\n")
        
        replay = input(f"Want to replay? 'Y' or 'N'")
        if replay.lower() == "y":
            start()
        else:
            print(f"\nOk, bye! :)")
    
    caesar(shift_direction=direction, plain_text=text, shift_amount=shift)


start()
