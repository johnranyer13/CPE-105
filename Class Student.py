class Student:
    name = ""
    course = ""

    def introduce(self):
        print("Hey I'm", self.name)

    def introduceAgain(self):
        print("I'm a", self.course)

person1 = Student()
person2 = Student()
person3 = Student()
person1.name = "Lyod"
person2.name = "John"
person3.name = "Mike"
person1.course = "Computer Engineering"
person2.course = "Electrical Engineering"
person3.course = "Graphics Technology"
person1.introduce()
person2.introduce()
person3.introduce()
person1.introduceAgain()
person2.introduceAgain()
person3.introduceAgain()
