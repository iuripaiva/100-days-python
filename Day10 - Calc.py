import arts

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():

    print(arts.calc_logo)

    num1 = float(input("What's the first number? "))

    should_continue = True

    while should_continue:

        for operator in operations:
            print(operator)
        operator_sym = input("Pick an operator from the line above: ")

        num2 = float(input("What's the next number? "))

        calc = operations[operator_sym]

        answer = calc(num1,num2)

        print(f"{num1} {operator_sym} {num2} = {answer}")

        redo = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if redo.lower() == "y":
            num1 = answer
        else:
            calculator()

calculator()