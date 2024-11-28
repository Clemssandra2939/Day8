# Part 4 - User Experience improvements ad final touch

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(start_text,shift_amount,cipher_direction):
     end_text = ""
     if cipher_direction == "decode":
        shift_amount *= -1  
     for char in start_text:
        #  TODO-3-What happens if the user enters a number/sybol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g start_text = "meet me at 3"
        end_text ="**** ** ** 3"

        position = alphabet.index(char)