import random

word_list = ["camel", "cow", "blade"]
lives = 6

wrd = random.choice(word_list)
#print(wrd)

placeholder = ""
for pos in wrd:
    placeholder += "_"
print(placeholder)    

game_over = False
correct_letters = []

while game_over == False:
    guessed_letter = input("Guess a letter!").lower()
    display = ""

    for letter in wrd:
        if letter == guessed_letter:
            display += letter
            correct_letters.append(guessed_letter)
        elif letter in correct_letters:
            display += letter    
        else:
            display += "_"    
    print(display)  
    
    if guessed_letter not in correct_letters:
        lives -= 1
    
    if "_" not in display:
        game_over = True
        print("U Win!")
    elif lives < 1:
        game_over = True
        print("U Lose!")