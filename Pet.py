class Pet:                          #SUPERCLASS
    petName = ""                    #MODIFIER "PUBLIC"
                                    
    def __init__(self):             #CONSRTRUCTOR
        self.petName = "Unknown"

    def getPetName(self):           #ACCESSOR
        return(self.petName)

    def setPetName(self, name):     #MUTATOR
        self.petName = name
        
    def speak(self):                #METHOD
        print("I'm your cuddly little pet.\n")

                                    
class Bird(Pet):                    #SUBCLASS
    def speak(self):                #METHOD
        print("I speak only when I want to.\n")

class Duck(Pet):                    #SUBCLASS
    def speak(self):                #METHOD
        print("Kwak Kwak")

#OBJECT
pet1 = Pet()
pet2 = Bird()
pet3 = Duck()

pet1.setPetName("Sun")
print("Hi, My name is", pet1.getPetName())
pet1.speak()

pet2.setPetName("Cha Cha")
print("Hi, My name is", pet2.getPetName())
pet2.speak()

pet3.setPetName("Donald Duck")
print("Hi, My name is", pet3.getPetName())
pet3.speak()
