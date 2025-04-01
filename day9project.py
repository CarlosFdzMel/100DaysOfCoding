# Secret Auction

import ASCIIart
print(ASCIIart.bid_logo)
print("\nWelcome to the auction")
Bid_End = False
participants = {}
winner = 0

while Bid_End == False:
    name = input("\nWhat is your name? ")
    bid = float(input("\nWhat is your bid? $"))
    participants[name] = bid
    
    if bid > winner: 
        winner = bid
        winner_name = name
    else:
        winner = winner

    New_Bidder = input("Are there any other bidder? (Type 'yes' or 'no'): ").lower()

    print("\n"*3000)


    if New_Bidder != "yes":
        print (f"The winner is {winner_name} with {winner} dollars")
        Bid_End = True
    