from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

answer = int


def calculator():

    print(f"{logo}")

    num1 = float(input("What is the first number?"))

    for symbol in operations:
        print(f"{symbol}")

    run = True

    while run:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number?"))
        calculate = operations[operation_symbol]
        answer = calculate(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.: ") == 'y':
            num1 = answer
        else:
            run = True
            calculator()


calculator()
