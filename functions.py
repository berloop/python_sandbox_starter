# A function is a block of code which executes only when it's called
# using a colon and identation
# identation is really important..use a formatter by any means..

# lets create a function
def sayILikeYou(name = 'Elizabeth Benneth'):
   print(f'I like you {name}!')

# Calling that defined function
sayILikeYou()


# Returning Values
def getProduct(num_1, num_2):
    product = num_1 * num_2
    return product
finalproduct = getProduct(4.5,2)
# Calling the defined function
print(finalproduct ,type(finalproduct))


# A lambda function is a small anonymous function
# A lambda function can take any number of arguments but can only have one expression

#  getSum = lambda num_1, num_2: num_1 + num_2
# print(getSum(45, 5))
def hellify(value):
    value = value * 2
    return value

print(hellify(5))