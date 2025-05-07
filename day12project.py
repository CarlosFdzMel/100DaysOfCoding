#Guess the number game
from ASCIIart import guess_num
import random

print(guess_num)
print("Welcome to the Number Guessing Game")
print("Guess the number between 1 and 100")
difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())
number = random.choice(range(1, 101))

def game(attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts")
        guess = int(input("\nMake a guess: "))
        if guess > number:
            print("Too high")
            attempts -= 1
            if attempts > 0:
                print("Guess again")
            else: 
                print ("No more attempts")

        if guess < number: 
            print ("Too low")
            attempts -= 1
            if attempts > 0:
                print("Guess again")
            else:
                print ("No more attempts")
        
        if guess == number:
            print(f"Congrats! The answer was {number}")
            attempts = 0
    
if difficulty == "easy":
    game(10)

elif difficulty == "hard":
    game(5)

else:
    print("INVALID INPUT")
