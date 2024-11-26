# Part 3: Reorganizing our code 

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt,type 'decode' to decrypt :\n")
text = input("Type your message:\n").lower()
shift =int(input("Type the shift number :\n"))

# TODO -1: Combine the encrypt() and decrypt() function into a single function called caesar()

def encrypt (plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)  # list_name . index(wat is the position of wat you are looking for the list) 
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")