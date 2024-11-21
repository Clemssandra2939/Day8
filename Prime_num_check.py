# Prime number can only be divided by one and itself and can't be divied into smaller number

# write a function thst checks whether if the number passed into it,is a prime number or not

# E.g 2 is a prime number becos it is can be divided by 2 and 2 itself

# But 4 is not a prime number becos you ca  divided by 1,2 or 4
# Try 1,2,3



n = int(input("Check this number : "))

def prime_checker(number):
    is_prime =True
    for i in range (2,number -1):
        if number % i == 0:
            is_prime ==  False
    if is_prime:
        print("it's a prime number")
    else:
        print("it's not a prime number")

prime_checker(number = n) #call function 

# i = 2 to 100