print("Welcolme to the tip calculator")
total = float(input("What was the total bill? $ "))
tip = int(input("Tip? 10% 12% or 15% "))
split = int(input("How many people to split the bill? "))

to_pay = round(((total *(tip/100))+total)/split, 2) 

print(f"Each person should pay: ${to_pay}")
