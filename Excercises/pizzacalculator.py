#Calcula la cuenta basado en las condiciones de la pizza 

print("Welcome to the delivery service")
size = str(input("What size pizza do you want? S, M, L: "))
pepperoni = str(input("Do you want pepperoni? Y or N: "))
extra_cheese = str(input("Do you want extra cheese? Y or N: "))

if size == "S":
    bill = 15
    print ("Small pizza costs $15")
elif size == "M":
    bill = 20
    print("Medium pizza costs $20")
elif size == "L":
    bill = 25
    print("Large pizza costs $25")
else: 
    print ("Incorrect input")

if pepperoni == "Y" and size == "S":
    bill +=2
    print ("Pepperoni for $2")
elif pepperoni == "Y" and size == "M" or size == "L":
    bill += 3
    print("Pepperoni for $3")

if extra_cheese == "Y":
    bill +=1
    print("Extra cheese for $1")

print(f"Your total bill will be: ${bill}")
