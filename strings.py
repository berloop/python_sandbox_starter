name = 'Abdul Mtoro'
age = 22

#concatenate
print('Hello, my name is ' + name + ' and am '+ str(age) + ' years old.')

#better string formatting

#Arguments by position
print ('My name is {name} and I am {age}'.format(name=name,age=age))

#F-Strings (way Easier)..
print (f'Hello, my name is {name} and I am {age}')

#String Methods..
message = 'hello World'

#Capitalize string..
print(message.capitalize())

# make all uppercase..
print(message.upper())

# make all lowercase..
print(message.lower())
# swap case
print(message.swapcase())

# Get length...
print(len(message))

# Replace..
print(message.replace('World','Everyone'))

#Count 'l' in the message..
sub = 'l'
print(message.count(sub))

# Starts with (bool)
print(message.startswith('hello'))

#end with (bool)
suffix ='d' 
print(message.endswith(suffix))

# Split into a list
print(message.split())

# Find a position
prefix = 'e'
print(message.find(prefix))

#Is all Alphanumeric(bool)
print(message.isalnum())

#Is all Alphabetic(bool)
print(message.isalpha())

#Is all Alphabetic(bool)
print(message.isnumeric())


# Create a list of words from a paragraph..
message = "In the Land of myth and the time of magic, the destiny of a great kingdom rests in the shoulder of a young man, His name was Merlin"
created_list = message.split()
len_list =len(created_list)
print(created_list.sort())