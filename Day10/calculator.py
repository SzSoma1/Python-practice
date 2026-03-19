def add (n1, n2):
    return n1 + n2

def multiply (n1, n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,    
}

def calculator():
    num1 = float(input("Give me the first number!: "))
    should_again = True

    while should_again:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Give me the operation symbol!: ")
        num2 = float(input("Give me the second number!: "))

        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input("Type 'y' to calculate with the result or type 'n' to a new calculation!: ")
        if choice == "y":
            num1 = result
        else:
            should_again = False
            print("\n"* 100)
            calculator()
            
calculator()