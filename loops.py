# Loop is used for iterating over a sequence (that's either a tuple, dictionary , or a set / string)

indieGames = ['Pinstripe','UnderTale','Ori','Borderlands','Darq','Once Upon a Coma','Equilinox']

# simple for loop
for indieGame in indieGames:
    print(f'Current Indie Game: {indieGame}')

# break (skips and terminate the loop)
for indieGame in indieGames:
    if indieGame == 'Ori':
        break
    print(f'Current Indie Game: {indieGame}')
    
# continue (skips and keep going until the loop terminates)
for indieGame in indieGames:
    if indieGame == 'UnderTale':
        continue
    print(f'Current Indie Game: {indieGame}')
    


 # range
for i in range(len(indieGames)):
    print(indieGames[i])
  
for i in range(0,11):
    print(f'Number: {i}')
    
 # While loop execute a set of statement as long as the condition is true
count = 0
while count < 1000000:
    print(f'Count: {count}')
  
    count += 1
    if count == 500:
        break
   