# ROCK, PAPER, SCISSORS GAME

Scissors = '''          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
                                   
                                   '''

Rock = '''                 _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                      '''

Paper = '''                             
                             
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              '''

game_images = [Rock, Paper, Scissors]


player_name = input("Enter your name: ")
player_movement = int(input("Type 1 for rock, 2 for paper and 3 for scissors: "))
if player_movement == 1: 
    print(game_images[0])
    print(f"\n{player_name} used Rock")

elif player_movement == 2: 
    print(game_images[1])
    print(f"\n{player_name} used Paper")

elif player_movement == 3: 
    print(game_images[2])
    print(f"\n{player_name} used Scissors")

else:
    print(f"{player_name} chose an invalid number. {player_name} lose")

import random
computer_movement = random.randint(1,3)
if computer_movement == 1 and player_movement <= 3 and player_movement >= 1: 
    print(game_images[0])
    print("\Computer used Rock")

elif computer_movement == 2 and player_movement <= 3 and player_movement >= 1: 
    print(game_images[1])
    print("\nComputer used Paper")

elif computer_movement == 3 and player_movement <= 3 and player_movement >= 1: 
    print(game_images[2])
    print("\nComputer used Scissors")


if player_movement <= 3 and player_movement >= 1:
    if player_movement == computer_movement:
        print("\n It's a tie!!!")
    elif player_movement == 1 and computer_movement == 2: 
        print("\n Computer wins!!!")
    elif player_movement == 2 and computer_movement == 3:
        print("\n Computer wins!!!")
    elif player_movement == 3 and computer_movement ==1: 
        print("\n Computer wins!!!")
    else: 
        print(f"\n {player_name} wins!!!")
