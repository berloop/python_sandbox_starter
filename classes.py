# A class is like a blueprint for creating objects. An Object has properties and methods (functions) associated with it. Almost everything in python is an object

# Creating a class

class Mutant:
    # Constructor - a function that runs when you instantiate an object from a class
    def __init__(self, name,age,killrate):
        self.name = name
        self.killrate = killrate
        self.age = age
    # remember the keyword 'this' in other languages I.e dart (this.name)
    
# Creating a method
    def mutantCall(self):
        # little calculations
        self.age -=500
        return f'The mutant {self.name}, Aged {self.age} years Old has a killrate of {self.killrate}/10'
   
   
# Extend class 
class ArcAngel(Mutant):
    # Constructor   
    def __init__(self, name,age,killrate):
        self.name = name
        self.killrate = killrate
        self.age = age
        self.glowIntensity = 0
        
    def set_glowIntensity(self,glowIntensity):
        self.glowIntensity = glowIntensity
        
        # Creating a method
    def mutantCall(self):
        # little calculations
        self.age +=500
        return f'The ArcAngel {self.name}, Aged {self.age} Million years Old has a killrate of {self.killrate}/10 and Glow Intensity of {self.glowIntensity}'
     
   
          
 # Init ArcAngel Object
Angel = ArcAngel('Jibril',2,10)
print(Angel.name)
Angel.set_glowIntensity(10.0)
print(Angel.mutantCall())
     
        
# Init mutant Object
Crawler = Mutant('NightCrawler',525,9.5)

# Accessing properties
print(Crawler.name)
print(Crawler.killrate)
print(Crawler.age)

# calling a function
print(Crawler.mutantCall())