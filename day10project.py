import ASCIIart
def addition(n1, n2):
    return n1 + n2

def substraction(n1,n2):
    return n1 - n2

def multiply(n1, n2): 
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

continue_calculus = True
operations = {"+" :addition,
              "-": substraction,
               "*": multiply,
               "/":divide,
                }

print(ASCIIart.calculator)
n1 = float(input("Give me the first number: "))
for symbols in operations: 
    symbol = print(symbols)


while continue_calculus: 

    math = str(input("\nSelect the operation: "))

    if math == "+": 
        n2 = float(input("\nGive the next number: "))
        result = operations["+"](n1,n2)
        print (f"{n1} + {n2} = {result}")

    elif math == "-": 
        n2 = float(input("\nGive the next number: "))
        result = operations["-"](n1,n2)
        print (f"{n1} - {n2} = {result}")

    elif math == "*": 
        n2 = float(input("\nGive the next number: "))
        result = operations["*"](n1,n2)
        print (f"{n1} * {n2} = {result}")

    elif math == "/": 
        n2 = float(input("\nGive the next number: "))
        result = operations["/"](n1,n2)
        print (f"{n1} / {n2} = {result}")

    use_number = str(input(f"\nYou want to use {result} for a new calculus? (y or n): ").lower())

    if use_number == "y": 
        n1=result
        for symbols in operations: 
            symbol = print(symbols)

    elif use_number != "y":
        print("\n"*1000)
        print(ASCIIart.calculator)
        n1 = float(input("Give me the first number: "))
        for symbols in operations: 
            symbol = print(symbols)
