# conditions..
# pretty basic

# do let's define some variables
num_x = 23.7
num_y = 25.7

if num_x > num_y:
  print (f'{num_x} is greater than {num_y}')
elif num_x == num_y:
  print (f'{num_x} is equal to {num_y}')
else:
  print(f'{num_y} is greater than {num_x}')

# Nested if
# if num_y > 2:
#     if num_y <= 10:
#         print ("This is not a cleaner way, Use logical Operators")

# Logical Operators

# and
if num_y > 2.0 and num_y <= 26.0:
    print("Get Ready for the night!")

# or
if num_y > 5.0 or num_x > 1.0:
  print("Get Ready for the weekend!")

# not
if not (num_x == num_y):
    print("Who's did that shit?")

# membership Operators (not, not in)
num = [1,2,3,4,5]
value = 15
# in
if value in num:
  print(value in num)
else:
  print('Not in the numbers')
# gives true or false

# not in
if value not in num:
  print(value not in num)
else:
 print('Among the numbers')
 
#  Identity Operators(is , is not) - Compare the objects not if they are equal,
#  but if they are actually the same object, with the same memory location:

# is
if value is 15:
  print(str(value is 15) + ' The Value is 17')
else:
  print('false')

# is not
if value is not 15:
  print(value is not 15)
else:
  print(str(value is 15) + ' The Value is 15')