# Termos aprendidos durante o day 2: 

# Data Types: String, Int, Float e Boolean
# Conversão de data types: int(), string(), float()
# Operadores matemáticos: + (soma), - (subtração), * (multiplicação), / (divisão), ** (exponente/potenciação)
# DICA: Sempre que se divide em python, o resultado é um float. MAS se usar // em vez de /, o resultado será inteiro. // = floor division: Converte a divisão pra int e arredonda se necessário.
# DICA2: PEMDAS -> lembrete da ordem de prioridade dos operadores: Parenteses, Expoente, Multiplicação, Divisão, Adição e Subtração
# Manupulação de numeros: +=, -=, /=, *= (usado pra incrementar ou remover algum valor de uma variavel, ex: score += 1)
# F-Strings: São strings que vc já coloca o valor da variável sem precisar concatenar, semelhante a template strings no JavaScript.
# EXEMPLO DE F-STRING: print(f"Your score is {score}.")


print("Welcome to the Tip Calculator\n")

totalbill = float(input("What was the total bill? $"))
totalppl = float(input("How many people to split the bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_percentage = (totalbill/100) * tip

finalvalue = round((totalbill+tip_percentage)/totalppl, 2)

print(f"Each person should pay: ${finalvalue}")