# A dictionary is a collection which is unordered, changeable and indexed.
# and it doesn't allow duplicate members.

# let us define some variables...
name = 'Abdul'
surname = 'Mtoro III'
age = 22
special_powers = 'Mind Reading'

# Even more variables...
name_1 = 'Zainab'
surname_1 = 'Adam'
age_1 = 22
special_powers_1 = 'Weather Manipulation'

# Create a single dictionary..
mutant = {
   'first_name':name,
   'last_name' :surname,
   'age':age,
   'special_powers': special_powers
}


# returning a dictionary with it's type..
print(mutant, type(mutant))

# use a constructor..
cons_mutant = dict(name=name,surname = surname)
#  get the keys..
print(cons_mutant['name'])

# or using get method
print(cons_mutant.get('surname'))

# Add key/value
cons_mutant['Origin'] = 'Xavier School of Gifted Youngsters'

# Get all the keys from a dictionary
print(cons_mutant.keys())

# Get dictionary items
print(cons_mutant.items())

# copying a dictionary and printing all the items..
clone_mutant = cons_mutant.copy()
print(clone_mutant.items())

# Adding a new key to a clone dictionary
clone_mutant['skin Colour'] = 'Blue Coloured'
print(clone_mutant.keys())


# Remove item
del(cons_mutant['Origin'])
print(cons_mutant.keys())

# or using pop method
clone_mutant.pop('skin Colour')
print(clone_mutant.keys())

# Clearing a dictionary
print(clone_mutant.clear())

# Get length of a dictionary
print(len(clone_mutant))

# Collection of Dictionaries
mutants = [
    # First dictionary
    {
        'name':name,
        'age':age,
        'Special Powers':special_powers
        },
     # Second dictionary
    {
        'name':name_1,
        'age':age_1,
        'Special Powers':special_powers_1
        
    },
]

# Printing multiple dictionaries
print(mutants)

# print specified keys from collections of dictionaries
print(mutants[1]['name'])

# Get length of items in the second dictionary
print(len(mutants[1]))


