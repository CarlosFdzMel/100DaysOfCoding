print(''' ,;~;,
                /\_
               (  /
               (()      //)
               | \\  ,,;;'\
           __ _(  )m=(((((((((((((================--------
         /'  ' '()/~' '.(, |
      ,;(      )||     |  ~
     ,;' \    /-(.;,   )
          ) /       ) /
         //  PjP    ||
        )_\         )_\ ''')

print("OHHH NO, THE PRINCESS WAS KIDNAPPED!!! WHAT OUR HERO WILL DO?")

start = input ("You want to look for the princess? (Y or N) ")
if start == "Y" or start == "y": 
    print ("\nThe king offers you a horse but you prefer to walk.")
    transport = input("What transport will you use? (Horse or Walk) \n ")
    if transport == "Horse" or transport == "horse" or transport == "HORSE":
        print("\nYou have been rinding for so long and you just arrived to a village ")
        ask = input("Who you interrogate for information? (Wizard or Seller) \n ")
        if ask == "Seller" or ask == "seller" or ask == "SELLER": 
            print("\nThe seller tells you the wizard kidnapped the princess")
            battle = input(" Do you confront the Wizard (Y or N) ")
            if battle == "Y" or battle == "y": 
                print("\n You captured the wizard and rescued the princess. CONGRATS!!!")
            elif battle == "N" or battle == "n": 
                print("The wizard transforms you into a frog. GAME OVER")
            else: 
                print("Invalid Input")

        elif ask == "Wizard" or ask == "wizard" or ask == "WIZARD":
            print("The wizard tricks you and sends you away. GAME OVER")
        else:
            print("Invalid Input")

    elif transport == "walk" or transport == "Walk" or transport == "WALK": 
        print("You were not fast enough. GAME OVER!")
    else:
        print("Invalid input")

elif start == "N" or start == "n": 
    print ("What a shame, the princess will be lost forever")

else:
    print ("Invalid input")
    