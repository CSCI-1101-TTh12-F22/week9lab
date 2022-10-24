### Functions

# Write a function that takes two integer arguments and returns True
# if the first is larger than the second, and False otherwise.

def bigger(a, b):
    if a > b:
        return True
    else:
        return False


# Write a function that takes two integers arguments and returns their
# product and their sum.


def integer_fun(a,b):
    return a*b, a+b

# Write another function that takes two
# integer arguments and calls the first function and returns 
# True if the product is larger than the sum, False otherwise.
def which_bigger(a,b):
    p,s = integer_fun(a,b)
    if p > s:
        return True
    else:
        return False


def main():

    i1 = 10
    i2 = 3

    # Then, write a main method that calls this function,
    # and based on what the function returns, prints out which of the two
    # ints is larger.
    if bigger(i1, i2):
        print(i1)
    else:
        print(i2)

    # Write a main function that calls the second function
    # and prints out a message like
    # "the sum of x and y is greater/less than the product of x and y"
    if which_bigger(i1, i2):
        print(f"the sum of {i1} and {i2} is less than the product of {i1} and {i2}")
    else:
        print(f"the sum of {i1} and {i2} is greater than the product of {i1} and {i2}")

    i1 = 1
    i2 = 3
    if which_bigger(i1, i2):
        print(f"the sum of {i1} and {i2} is less than the product of {i1} and {i2}")
    else:
        print(f"the sum of {i1} and {i2} is greater than the product of {i1} and {i2}")

main()
