# Termos aprendidos durante o day 1: 

# Função print()
# DICA: Pra pular linha usando somente um comando de print, em vez de ficar usando vários, é só usar
# o termo "\n" no meio da string.
# Manipulação de strings (concatenação ).

# Debugging iniciante: Atenção a Typos (erros tipográficos/erros de escrita).

# Função input().

# DICA: Pra imprimir uma resposta a um input usando uma só linha de código, dá pra fazer da forma abaixo:
    # print("Olá, " + input("Qual é o seu nome? ") + "!")
    # O resultado impresso será "Olá, {seu nome}!"

# Variáveis

# DESAFIO FINAL DO DIA 1:

print("Hello! This is the Band Name Generator.\n")

city = input("What's the name of the city you grew up in?\n")

pet = input("What's your pet's name?\n")

bandname = (f"{city} {pet}")

print (f"Your band name could be {bandname}")