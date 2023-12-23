print("Welcome to the Tip Calculator\n")

totalbill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))
totalppl = int(input("How many people are going to split the bill? "))
tip_percentage = totalbill * (tip/100)

finalvalue = format((totalbill+tip_percentage)/totalppl, '.2f') # Esse '.2f' é usado com a função round() pra exibir 2 digitos após o ponto. ATENÇÃO: O resultado será string.

print(f"Each person should pay: ${finalvalue}")
