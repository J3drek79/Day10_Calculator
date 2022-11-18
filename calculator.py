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

num1 = int(input("What is the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = (input("Pick an operation from the line above: "))
num2 = int(input("What is the second number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(n1=num1, n2=num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = (input("Pick another operation from the line above: "))
num3 = int(input("What is the second number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(n1=first_answer, n2=num3)

print(f"{first_answer} {operation_symbol} {num2} = {second_answer}")
