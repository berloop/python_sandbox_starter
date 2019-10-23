# A tuple is a collection which is ordered and unchangeable..
# Allows duplicate members...

fruits = ('Peach','Bananas','Pineapples')
fruits_tupple = tuple(('Peach','Bananas','Pineapples'))

# Single Value needs a trailing coma..
fruits_tupple_new = ('Peach',)

print(fruits,fruits_tupple)
# A set is a collection which is unordered and unindexed...

print(fruits,type(fruits_tupple))
print(fruits_tupple[1])

# Can't change value
# fruits_tupple[0] = 'Peach'
print(fruits_tupple)

# Delete tuple
del fruits_tupple

print (len(fruits))


# Create set
fruits_set = {'Peach','Oranges','Pomengranate'}

#  Check if in set
print ('Peach' in fruits_set)

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

# Add duplicate
fruits_set('Oranges')
print(fruits_set)

# Remove from set
fruits_set.remove('Grapes')
print(fruits_set)

# Clear set(differs from deleting..Leaves Empty set)
fruits_set.clear()
print(fruits_set)
