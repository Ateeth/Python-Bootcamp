alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(direction , text , shift) :
    if direction == 'decode' :
        shift *= -1
    end_text = ""
    for letter in text:
        if letter not in alphabet :
            end_text += letter
        else :
            end_text += alphabet[(alphabet.index(letter) + shift) % 26]
    print(f"The {direction} text is {end_text}")

# def encrypt(text , shift) :
#   encrypted = ""
#   for letter in text :
#     encrypted += alphabet[(alphabet.index(letter) + shift) % 26]
#   print(f"The encoded text is {encrypted}")
#
# def decrypt(text , shift) :
#   decrypted = ""
#   for letter in text :
#     decrypted += alphabet[(alphabet.index(letter) - shift) % 26]
#   print(f"The encoded text is {decrypted}")

from art import logo

print(logo)
run_code_again = 'yes'

while run_code_again == 'yes' :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(direction, text, shift)

    run_code_again = input("Do you want to run the cipher again ? ")

print("Goodbye :)")