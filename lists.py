# list allows duplicate members..

# Create List
numbers = [1,2,3,4,5]
fruits = ['Pomengranate','Oranges','Peach']

# Use a constructor
numbers_cons = list((1,2,3,4,5))

print(numbers,numbers_cons)

# Get a value
print(fruits[1])

# Get Length
print(len(fruits))

# Append to list
fruits.append('Mangoes')
print(fruits)

# Insert into position
index = 2
new_fruit = 'Strawberries'
fruits.insert(index,new_fruit)
print(fruits)

# Remove from list
fruits.remove('Peach')
print(fruits)

# Change value
fruits[0] = 'Blueberries'


# Remove from position
fruits.pop(index)
print(fruits)

# Reverse the members..
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=False)
print(fruits)