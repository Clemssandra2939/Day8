

# # Number manipulation

# # print(int(8/3))
# # # to round a float or decimal number to a whole number or an integer
# # print(round(8/3))
# # # to round to a decimal places like two decimals or three decimal places
# # print(round(8/3,2))
# # to straight up convert to interger without having to do print(type()) do this when it comes to float when u check the type instead of float it will give an intger
# # print(type(8//3))
# # it is called the floor division
# # when you want to continue a calculation or contine performing a calculations in this variable
# # eg if this result is saved in a variable


# # result=(4/2)
# # result/=2
# # print(result)
# # # this /= can go with - + / * 


# # **********F strings(it is useresult=(4/2)
# # result/=2
# # print(result)
# # # this /= can go with - + / * 



# # *******F strings(used to mix strings and different data types)
# # in this situation where they is alot to converse and to do it in a single way where there is alot of data types
# # score= 0
# # height=1.8
# # isWinning=True
# # # u use (f""),
# # print(f"your score is {score},your height is {height} ,you are winning is{isWinning}")



# # last coding challenge_for day 2-ur life in weeks
# # create a program using maths and f strings that tel us how many days,weeks,months we hv left if we live until 90years



# # current_age=input("what is ur current age?")
# # target_age=input("what is ur target age?")

# # days_remaining=(int(target_age)-int(current_age))*365

# # weeks_remaining =(int(target_age)-int(current_age))*52

# # months_remaining=(int(target_age)-int(current_age))*12

# # print(f"you have {days_remaining}days,{weeks_remaining}weeks,{months_remaining}months left")


# # Tip calculator program
# print("Welcome to the tip calculator")
# total_bill=(input("what is the total_bill? $"))
# print(total_bill)
# percentage_tip=(input("what is the percentage_tip would u like to give? 10,12 or 15 "))
# print(percentage_tip)
# num_people=(input("how many people to split the bills?"))
# print(num_people)
# percentage_number=(int(percentage_tip)/100)
# print(percentage_number)
# Everyones_bill =int(total_bill) * float(percentage_number)
# result=int(Everyones_bill)+ int(total_bill)
# print(result)
# result/=int(num_people)
# print(result)
# print(f"Each person should pay:{result}$")
# # if the bill was 150.00,split btw 7 people,with 12% tip.
# # Each person should pay(150.00/5)*0.12
# # Round up to two decimal places





# # year=int(input("which year do u want to check? "))
# # if year % 4==0:
# #     if year % 100==0:

# #         if year % 400==0:
# #             print(f"{year} is leap year")
# #         else: 
# #             print(f"{year} is not leap year")
# #     else:
# #         print(f"{year} is leap year")

# # else:
# #     print(f"{year} is not leap year")




# # Password Generator Program
# import random
# letters =['a','b','c','d','e','f','g','h','i','j','k','l','m',
# 'n','o','p','q','r','s','t','u','v','w','x','y','z',
# 'A','B','C','D','E','F','G','H','I','J','K','L','M',
# 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# numbers =['0','1','2','3','4','5','5','6','7','8','9']
# symbols =['!','#','$','%','&','(',')','*','+']

# # password =[letters,numbers,symbols]

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like? \n"))
# nr_numbers =int(input(f"How many numbers would you like?\n"))
# # password =[letters,numbers,symbols]

# # random_password = random.randint(0,password - 1)
# # print(password[random_password])

# # Easy Level
# # password = ""

# # for char in range(1,nr_letters + 1):
# #     password += random.choice(letters)

# # for char in range(1,nr_symbols + 1):
# #     password += random.choice(symbols)

# # for char in range(1,nr_numbers + 1):
# #     password += random.choice(numbers)

# # print(password)

# # Hard level
# password_list = []

# for char in range(1,nr_letters + 1):
#     password_list += random.choice(letters)

# for char in range(1,nr_symbols + 1):
#     password_list += random.choice(symbols)

# for char in range(1,nr_numbers + 1):
#     password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#     password += char

# print(f"Your password is: {password}")


# Python list index() Method
fruits = ["apple","banana","cherry"]
x = fruits.index("cherry")

print(x)


# Step 5

import random

# TODO - 1 : - Update the word list to use the 'word_list'from hangman_word.py

from hangman_words import word_list
chosen_word =random.choice(word_list)
word_length =len(chosen_word)



Game_Over = False
lives = 6

# TODO - 3 : - import the logo from hangman- art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

# Testing code
print(f"Psst,the solution is {chosen_word}") 

# Create blanks
display =[]
for _ in range(word_length):
    display += "_"


while not Game_Over :
    guess = input ("Guess a letter:").lower()

    

    # TODO - 4 : - If the user has entered a letter they have already guessed,print the letter and let them know.
    if guess in display:
        print(f"You have already guessed{guess}")
 # Check guessed letter

    for position in range(word_length):
        letter = chosen_word [position]
        # print(f"Current postion:{position}\n Current letter :{letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO - 5 : - If the letter is not in the chosen_word,print out the letter and let them know it's not in the word
         print (f"You guessed {guess},that's not in the word.You lose a life")
         lives -= 1
         if lives == 0:
                Game_Over = True
                print("You lose!!")
     
    # Join all the element in the list and turn it into a String.
    print(f"{' '.join(display)}")


    # Check if user has got all letters.
    if "_"  not in display:
        Game_Over = True
        print("You Win!!")

    # TODO - 2 : - import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
   
# Nested if/ else statement
# if conditon:
#     if another codition:
#        do this
#     else:
#         do this
# else:
#     do this        

# # Roller coaster program
# print("print(f"Your love score is {love_score}")welcome to the rollercoaster!")
# height=int(input("what is ur height in cm?"))

# if height > 120:
#     print("u can ride the rollercoaster!")
#     age=int(input("what is ur age?"))

#     if age < 12:
#       print("pay 5$")
#     elif age <= 18:
#         print("Pay 7$")
#     else:
#        print("Pay 12$")
# else:
#   print("Sorry,u have to grow taller before u can ride.")

#   here if they are below 12 they pay 5$ 
# if they are 12 to 18 they pay $7 buh if they greater than 18 they pay adult price 12$

# this where elif comes,it comes btw any if and else statement
# if condition1:
#     do A
# elif conditon2:
#     do B
# else:
#     do this