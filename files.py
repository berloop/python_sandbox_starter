# Functions for CRUD Files

# Open a file
myFile = open('LoveLetter.txt','w')

#Get info
print('Name: ',myFile.name)
print('Is Closed: ',myFile.closed)
print('Is Opened: ',myFile.mode)

# Write to file
myFile.write('My Love for You has found the boundaries i can break')
myFile.write(' ')
myFile.close()

# Append to file
myFile = open('loveLetter.txt','a')
myFile.write("and I love Only You My Love Anabelle Lee!")
myFile.close()

#Read from file
myFile = myFile = open('loveLetter.txt','r+')
text = myFile.read(100)
print(f'Lovemessage: {text}')