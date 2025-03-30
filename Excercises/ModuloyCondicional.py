# Pregunta por un numero y devuelve si es par o impar

num = int(input("Give me a number: "))
par_impar = num % 2

if par_impar == 0:
    print("Your number is even")
else:
    print("Your number is odd")
