# The blackjack game
import random
import ASCIIart

def deal_card(): 
    """"Returns a random card from the deck"""
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def score(cards):
     """Returns the score of the cards"""
     if sum(cards)==21 and len(cards)==2: 
        return 0 
     
     if 11 in cards and sum(cards) > 21: 
         cards.remove(11)
         cards.append(1)

     return sum(cards)

def winner(player_score, computer_score):
    if player_score == 0: 
        return "Blackjack!! You win"
    elif computer_score == 0: 
        return "Blackjack!! Computer wins"
    elif player_score > 21: 
        return "BUST! Your score is over 21"
    elif computer_score > 21: 
        return "BUST! Computer's score is over 21"
    elif player_score == computer_score: 
        return "DRAW!"
    elif player_score > computer_score:
        return "You win!"
    else: 
        return "Computer wins!"

def blak_jack_game():
    print(ASCIIart.cards)
    player_cards = []
    computer_cards = []
    computer_score = -1
    player_score = -1
    game_over = False

    for _ in range(2): 
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over: 
        player_score = score(player_cards)
        computer_score = score(computer_cards)

        print(f"Your cards are: {player_cards}. Total score: {player_score}")
        print(f"Computer's first card is: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True

        else: 
            draw = str(input("\nYou want to draw a card? (y or n) ").lower())

            if draw == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17: 
        computer_cards.append(deal_card())
        computer_score = score(computer_cards)

    print(f"\nYour final cards are: {player_cards}. Total score: {player_score}")
    print(f"Computer's final cards are: {computer_cards}. Total score: {computer_score}")
    print(winner(player_score, computer_score))


while input("\nYou want to play Blackjack? (yes or no) ").lower() == "yes":
    print("\n"*60)
    blak_jack_game()
