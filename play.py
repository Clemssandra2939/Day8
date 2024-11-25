

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