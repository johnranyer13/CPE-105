class Car:
    __ownerName = ""
    def __init__(self):
        self.__ownerName = "Unknown"

    #ACCESSOR
    def getOwnerName(self):
        return (self.__ownerName)

    #MUTATOR
    def setOwnerName(self, name):
        self.__ownerName = name

owner1 = Car()
owner1.ownerName = "Mon"
owner1.setOwnerName ("Jay")
print(owner1.getOwnerName())
