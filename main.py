print("welcome to the bmi calculator")
weight = float(input("pls insert your weight"))
height = float(input("pls insert your height"))
bmi = float((weight)/(height*2))

print(f"your bmi is {bmi}.")
if bmi <= 18.5:
   print("You are underweight")
elif bmi < 25:
   print("you have a normal weight")
elif bmi < 30:
    print("slightly overweight")
elif bmi < 35:
    print("obese")