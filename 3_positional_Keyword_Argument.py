# Function that allows multiple input
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"wat is it like in {location}")

# greet_with("Sandra", "Enugu")

# when the postion of the data is switched like
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"wat is it like in {location}")

# greet_with("Enugu", "Sandra")

# this wat it is goinh to be like
# ##Hello Enugu
# Wwat is it like in Sandra

# placing it in the wrong parameters,this is called postional argument

# Keyword arguemnt

# Keyword argument is a way of resolving those kind of errors of poistional argument
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"wat is it like in {location}")

greet_with(location = "Enugu", name = "Sandra")