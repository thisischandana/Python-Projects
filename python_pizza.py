print("welcome to python pizza")
size = input("choose your size 'S', 'M', 'L'")
add_pepp = input("do u want to add pepporoni 'YES' or 'NO' ").lower()
add_cheese = input("do u want to add cheese? 'y' or 'n' ").lower()
bill = 0
if size == 'S':
    bill += 15
    add_pepp == 'yes'
    bill += 2
    add_cheese == 'y'
    bill += 1
if size == 'M':
    bill += 20
    bill += 15
    add_pepp == 'yes'
    bill += 2
    add_cheese == 'y'
    bill += 1
if size == 'L':
    bill += 25
    add_pepp = 'yes'
    bill += 3
    add_cheese ='y'
    bill += 1
print(f"your bill is {bill}")


