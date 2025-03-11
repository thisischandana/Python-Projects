import random
print("welcome to password generator")
letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*']

numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
letter_count = int(input("how many letter do you want to keep in your password"))
symbol_count = int(input("how many symbol do you want to keep in your password"))
number_count = int(input("how many number do you want to keep in your password"))
password = []
for i in range(0, letter_count):
    computerised_letter = random.choice(letters_list)
    password += computerised_letter
for i in range(1, symbol_count+1):
    computerised_symbol = random.choice(symbol_list)
    password += computerised_symbol
for i in range(1, number_count+1):
    computerised_number = random.choice(numbers_list)
    password += computerised_number
print(password)
random.shuffle(password)
print(password)
new_password = ""
for i in password:
    new_password += i
print(new_password)



