#create a random word
import random
word_list = ['foamy','hello', 'burger','sweet','doctor','koushik']
random_word = random.choice(word_list)
print(random_word)

#create a blank till the length of the random_word
store = []
for i in random_word:
    store += "_"
print(store)

#ask the user to guess a letter
lives = 6
end = False
while end == False:

    user_guess = input("guess a letter")
    #check if the guessed letter is in the random word
    for i in range(len(random_word)):
        current_letter = random_word[i]
        if current_letter == user_guess:
            store[i] = current_letter
    print(store)

    if user_guess not in random_word:
        lives -=1
        print(f"you have {lives} chances left")
        if lives == 0:
            print("you lose!")
            break



if "_" not in store:
    end == True




