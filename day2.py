# Termos aprendidos durante o day 2: 

# Data Types: String, Int, Float e Boolean

# Conversão de data types: int(), string(), float()

# Operadores matemáticos: + (soma), - (subtração), * (multiplicação), / (divisão), ** (exponente/potenciação)

# DICA: Sempre que se divide em python, o resultado é um float. MAS se usar // em vez de /, o resultado será inteiro. // = floor division: Converte a divisão pra int e arredonda se necessário.

# DICA2: PEMDAS -> lembrete da ordem de prioridade dos operadores: Parenteses, Expoente, Multiplicação, Divisão, Adição e Subtração.

# Manupulação de numeros: +=, -=, /=, *= (usado pra incrementar ou remover algum valor de uma variavel, ex: score += 1).

# F-Strings: São strings que vc já coloca o valor da variável sem precisar concatenar, semelhante a template strings no JavaScript.

# EXEMPLO DE F-STRING: print(f"Your score is {score}.")

# DESAFIO FINAL DO DIA 2:

print("Welcome to the Tip Calculator\n")

totalbill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))
totalppl = int(input("How many people are going to split the bill? "))
tip_percentage = totalbill * (tip/100)

finalvalue = format((totalbill+tip_percentage)/totalppl, '.2f') # Esse '.2f' é usado com a função round() pra exibir 2 digitos após o ponto. ATENÇÃO: O resultado será string.

print(f"Each person should pay: ${finalvalue}")