from art import logo

# Adition
def add (n1, n2):
    return n1 + n2

# Substraction
def substract (n1, n2):
    return n1 - n2

# Multiplication
def multiply (n1, n2):
    return n1 * n2

# Division
def divide (n1, n2):
    return n1 / n2

def calc(num1):
    for operation in operations:
        print(operation)

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    print(f"{num1} {operation_symbol} {num2} = {calculation_function(num1, num2)}")
    return calculation_function(num1, num2)    


print(logo) 

operations = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide,
}

answer = float(input("What's the first number? "))

while True:
    answer = calc(answer)
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if choice.lower() == 'y':
        continue
    else:
        break