import random
letter = ['a', 'b', 'c', 'd']
symbol = ['#', '$', '*', '&']
password = ""
print("welcome to random password generator")
letter_number = int(input("how many letters would you like in your password?"))
symbol_number = int(input("how many symbols you want in your password"))
for letter in range(1, letter_number+1):
    password += random.choice(letter)

for symbol in range(0, symbol_number):
    password += random.choice(symbol)


print(password)

