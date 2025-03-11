year = int(input("enter a year"))
if year % 4 == 0:
    print("leap year")
    if year % 100 == 0:
        print("not a leap year")
        if year % 400 == 0:
          print("leap year")
else:
    print("not a leap year")