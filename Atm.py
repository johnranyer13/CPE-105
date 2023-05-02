class Atm:
    __ownerName = ""
    __money = ""

    def __init__(self, bal=500):
        self.__ownerName = "Unknown"
        self.__money = bal
        
    def getOwnerName(self):
        return(self.__ownerName)

    def getMoney(self):
        return(self.__money)

    def setOwnerName(self, name):
        self.__ownerName = name

    def setMoney(self, bal):
        self.__money = bal

owner1 = Atm()
owner2 = Atm()
owner1.setOwnerName("Adam")
owner2.setOwnerName("Ben")
owner1.setMoney("7000")
owner2.setMoney("10000")
print(owner1.getOwnerName(), "money balance is:", owner1.getMoney())
print(owner2.getOwnerName(), "money balance is:", owner2.getMoney())
