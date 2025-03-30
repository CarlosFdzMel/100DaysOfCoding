#Elige al azar una persona que pagará la cuenta
import random

names = ["Carlos", "Rafael", "Ariel", "Alejandro", "Joel", "Arturo", "Diego", "Alexis"]
chosen = random.randint(0,7)
who_will_pay = names[chosen]
print (who_will_pay)

