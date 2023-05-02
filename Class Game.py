class Game:
    category = ""

    def getCategory(self):
        print("I wiil choose", self.category)

ML = Game()
ML.category = "Multiple Player"
ML.getCategory()
