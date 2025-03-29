# Part 1: Generates de password as letter-number-symbol
print("This code generates a random password")
import random
#Letters= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Letters = Low + Up
Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Symbols = ["#", "$", "%", "&", "?", "+", "@", "(" , ")", "*"]

num_lett = int(input("How many letters do you want in your password? "))
num_num = int(input("How many numbers do you want in your password? "))
num_symb = int(input("How many symbols do you want in your password? "))

password = ""

for char in range(0, num_lett):
    password += random.choice(Letters)

for char in range(0, num_num):
    password += random.choice(Numbers)

for char in range(0, num_symb):
    password += random.choice(Symbols) 

print(f"Your password coud be: {password}")

# Part 2: Generates the password in a random way
password_list = []
for char in range(0, num_lett):
    password_list.append(random.choice(Letters))

for char in range(0, num_num):
    password_list.append(random.choice(Numbers))

for char in range(0, num_symb):
    password_list.append(random.choice(Symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"A stronger password could be: {password}")
