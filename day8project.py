# Caesar Cipher
import ASCIIart
print (ASCIIart.caesar_cypher_logo)

print("Encode or Decode a message")
alphabeth = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Continue_Program = "yes"

def encrypt(text,shift):
    display = ""

    for letters in text:

        if letters not in alphabeth: 
            display += letters

        else: 
            new_alphabeth = (alphabeth.index(letters) + shift)
            if new_alphabeth > 25: 
                new_alphabeth = alphabeth.index(letters) -26 + shift
            coded_text = alphabeth[new_alphabeth] 
            display += coded_text

    print(f"\nThe encoded message is: {display}") 

def decrypt(text, shift):
    display = ""

    for letters in text:

        if letters not in alphabeth: 
            display += letters

        else:
            decoding_alphabet = alphabeth.index(letters) - shift
            decoded_text = alphabeth[decoding_alphabet]
            display += decoded_text

    print(f"\nThe decoded message is: {display}")

def cesar(direction): 
    if direction == "encode":
        encrypt(text, shift)
    
    elif direction == "decode": 
        decrypt(text,shift)
    
    else: 
        print("Inavlid command")

while Continue_Program == "yes":
    direction = input("\nType 'encode' or 'decode': \n").lower()
    text = input("Write your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    cesar(direction)
    Continue_Program = input("\nType 'yes' to continue, type 'no' to exit: ").lower()

if Continue_Program != "yes":
    print("\nSee you later")
