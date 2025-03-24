import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Hint1: Create a function that uses a list below to return a random card

def deal_card():
    random_card = random.choice(cards)
    return random_card
    """ Deal the user and computer 2 cards each using deal_card() and append()"""


def calculate_score(cards):
    """take the list of cards and returns the score of sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    """ take some cards as input and calculate the total"""
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "win with a blackjack"
    elif user_score> 21:
        return "you went over, you lose"
    elif computer_score>21:
        return "opponent went over, you win"
    elif user_score>computer_score:
        return "you win"
    else:
        return "you lose"



user_cards = []
computer_cards = []
computer_score = -1
is_game_over = False
user_score = -1

is_game_over = False
for i in range(0, 2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" your cards : {user_cards} and your score: {user_score}")
    print(f" computers first card {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' for yes ")
        if user_should_deal == 'y':
           user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score<17:
    computer_cards.append((deal_card()))
    computer_score = calculate_score(computer_cards)

print(compare(computer_score, user_score))



