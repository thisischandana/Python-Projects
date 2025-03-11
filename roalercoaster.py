height = int(input("enter your height"))
age = int(input("enter your age"))
bill = 0
want_photos = input("'yes' or 'no'").lower()
if height > 120:
    print("yay! you can ride the roalercoaster")
    if age < 12:
        bill += 5
        if want_photos == 'yes':
            bill += 3
    if age > 18:
        bill += 12
        if want_photos == 'yes':
            bill += 3
    if age in range(12, 18):
        bill += 7
        if want_photos == 'yes':
            bill += 3
else:
    print("you cant ride the roalercoaster")


print(bill)
