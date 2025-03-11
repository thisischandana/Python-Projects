import random
life = 6
word_list = ['avacado', 'apple', 'bananana']
random_word = random.choice(word_list)
print(random_word)
#generate as many blanks as letters in word
blanks =" "
for i in random_word:
    blanks += "__, "
print(blanks)
#ask the user to guess a letter
user_guess = input("guess your letter: ")
display = " "
for letter in random_word:
    if letter == user_guess:
        display += letter
    else:
        display += "_"
        life -= 1
print(display)
print(f"you have {life} lives left")


