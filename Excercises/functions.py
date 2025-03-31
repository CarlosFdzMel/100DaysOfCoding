# Funciones
def greet(): 
    print("Hello")
    print("My name is")
    print("Carlos")

greet()

# Funciones con una entrada

def greet_name(name): 
    print(f"\nHello {name}")
    print(f"How are you today {name}")
    print(f"Hope you a nice day, {name}")

greet_name("Carlos")

#Funciones con más de una entrada

def greet_loc(name, location): 
    print(f"\nMay I ask you a question {name}?")
    print(f"What's the temperature at {location}?")

greet_loc("Carlos", "Querétaro") # Usando posición
greet_loc(location="Querétaro", name="Carlos") # Usando palabra clave
