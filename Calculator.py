def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "%" : divide
}
def calculator():

        should_continue = True
        num1 = int(input("Enter the first number"))

        while should_continue:
            for symbol in operation:
                print(symbol)
            operation_symbol = input("enter the operation")
            num2 = int(input("Enter the second number"))
            answer = (operation[operation_symbol](num1, num2))
            print(f"{num1}{operation_symbol}{num2} = {answer}")
            choice = input("Type 'y' to continue and 'n' to continue with {answer} and 'n' to stop the calculation")
            if choice == 'y':
                num1 = answer
            else:
                should_continue = False
                print("\n"*100)
calculator()