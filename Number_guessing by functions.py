#choosing a random number from 1 to 100.
import random
computer_guess = random.randint(1,100)
chances_left = 10


#Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty level: 'Easy' or 'Hard'")
    if level == 'Easy':
        return chances_left
    elif level == 'Hard':
        return chances_left - 5



#Let the user guess a number
user_guess = int(input("Guess a number: "))


#Function to check users guess against actual answer
def check_guess(users_guess, actual_guess):
    if users_guess == actual_guess:
        print("Hey! You won!")
    elif users_guess != actual_guess:
        return chances_left - 1


#Track the number of turns and reduce it by 1



#Repeat the guessing functionality if they get it wrong


