import random
chances_left = 10
computer_choice = random.randint(0,100)
difficulty_level = input("Choose 'Easy' or 'Hard' difficulty level")
if difficulty_level == 'Easy':
    chances_left = 10
else:
    chances_left = 5

should_continue = True
while should_continue:
    user_choice = int(input("Enter any number"))

    if user_choice == computer_choice:
        print(f"the answer was {computer_choice}")
        print("You have got the answer! You won!")
        break
    else:
        chances_left -= 1
        if user_choice < computer_choice:
            print("Too low")
        elif user_choice > computer_choice:
            print("Two high")
        elif user_choice != computer_choice:
            print("Hey! Guess again")
        print(f"the answer was {computer_choice}")
        print(f"You have {chances_left} chances left.")
        if chances_left == 0:
            should_continue = False
