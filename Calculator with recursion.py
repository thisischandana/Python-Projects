def add(n1, n2):
    return n1+ n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2



def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    should_continue = True
    num1 = float(input("enter the first number "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("choose your operation ")
        num2 = float(input("enter the second number "))

        answer = operations[operation_symbol](num1, num2)
        print(answer)
        choice = input("whether you want to continue the calculation or not? type 'y' or 'n' ")
        if choice == "y":
            num1 = answer
        else:
            should_continue = False

calculator()



