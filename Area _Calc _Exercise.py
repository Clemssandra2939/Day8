# ReadMe Instructions
# You are painting a wall.The instructions on the point can say that 1 can of paint can cover 8 square meters of wall.
# Given a random height and width of wall,calculate how many can of paint you will need to buy.

# number_of_cans =(wall height * wall width) /  coverage per can.

# E.g Height = 2, Width = 4, Coverage = 5
# number_of_cans =(2 * 4) / 5   #1.6

# But bcos you can't buy 0.6 of a can of paint,the result should be rounded up to 2 cans

# Important:Notice the name of the function and parameter must match those on line 13 for the code to work

# Example Input:
# test_h = 3
# test_w = 9

# Example Output:
# You'll need 6 can of paint.

# Hint:
# To round up the number_of_can
# Make sure you name your function/parameters the same as when it's called on the last line of code