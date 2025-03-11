
num = int(input("insert a number to check whether it is prime or not"))
def prime_number(n):
    is_prime = True
    for i in range(2, n):
        if num % i == 0:
            is_prime = False
    if is_prime == True:
        print("this is prime")
    else:
        print("this is not a prime number")

prime_number(n=num)