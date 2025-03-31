# THE HANGMAN GAME
import random
import hangmanART
import hangmanWORDS

chosen_word = random.choice(hangmanWORDS.words)
word_length = len(chosen_word)
save = []
errors = []
Game_Over = False
lives = 6

print(hangmanART.logo)
print("\n *********** YOU HAVE 6/6 LIVES *****************")

blanks = "" 
for num_blanks in range(word_length):
    blanks += "_ "
print (blanks)


while Game_Over == False:
    guess = str(input("\nGive me a letter: ")).lower()
    display = ""

    if guess in save:
        print (f"\n ******** YOU DON'T HAVE TO TYPE {guess} AGAIN *************")
    elif guess in errors: 
        print(f"\n ********* YOU KNOW {guess} IS NOT IN THE WORD. YOU LOSE A LIFE *******")

    for letter in chosen_word: 

        if guess == letter:
            display += letter
            save.append(letter)

        elif letter in save:
            display += letter

        else: 
            display += "_ "
            errors.append(guess)
            
    
    if guess not in chosen_word : 
        lives -= 1
        # HERE YOU CAN WRITE THE CONDITION OF REPETED WRONG LETTERS. IT AVOIDS THE ERRORS LIST#
        print(f"\n *********** YOU HAVE {lives}/6 LIVES *****************")
        print (hangmanART.DRAWS[lives])
    
    print (display)

    if "_" not in display: 
        Game_Over = True
        print(f"\n  **************** {chosen_word} WAS CORRECT. YOU WIN!! **************")

    if lives == 0: 
        Game_Over = True
        print(f" ************************* {chosen_word} WAS THE CORRECT ONE. GAME OVER!   *******************************")
