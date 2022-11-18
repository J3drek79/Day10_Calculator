# Calculator

#Add
def add(n1, n2):
    """Add vaues"""
    return n1 + n2

#Substract
def substract(n1, n2):
    """Substract values"""
    return n1 - n2

#Multiply
def multiply (n1, n2):
    """Multiply values"""
    return n1 * n2

#Divide
def divide (n1, n2):
    """Divide values"""
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    shouldend = False
    while not shouldend:
        operation_symbol = (input("Pick an operation: "))
        num2 = int(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1=num1, n2=num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            shouldend = True
            calculator()
calculator()
