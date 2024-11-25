# Part 2 - Decryption

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt,type 'decode' to decrypt :\n")
text = input("Type your message:\n").lower()
shift =int(input("Type the shift number :\n"))

def encrypt (plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)  # list_name . index(wat is the position of wat you are looking for the list) 
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

# TODO-1- Create a different function called 'decrypt' that takes the 'text' and 
# 'shift' as inputs.
def decrypt (plain_text,shift_amount):
    decode_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)  # list_name . index(wat is the position of wat you are looking for the list) 
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decode_text -= new_letter
    print(f"The decoded text is {decode_text}")
# TODO-2- Inside the 'decrypt' function,shift each letter of the 'text' *backwards*
# in the alphabetby the shift amount and print the decrypted text 
# E.g 
# cipher_text = "mjqqt"
# shift = 5
# plain text =  "hello"
# print output : "The decoded text is "hello"

# TODO-3- Check if the user wanted to encrypt or decrypt the messages by checking the 'direction' variable,Then call the correct function based on that 
# 'direction'variable .You should be able to text the code to encrypt*AND* decrypt a message.
if direction == encrypt:
    print

