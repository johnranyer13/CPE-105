class Person:


    def __init__(self, gender):
        self.gender = gender

    def displayGender(self):
        print("I'M A", self.gender)

gen1 = Person("Boy")
gen2 = Person("Girl")
gen3 = Person("Lesbian")
gen4 = Person("Gay")

gen1.displayGender()
gen2.displayGender()
gen3.displayGender()
gen4.displayGender()
