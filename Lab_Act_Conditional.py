#Script 1
"""
x = 2
print (x == 2)
print (x == 3)
print (x < 3)
print ("\n")

#Script 2
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.\n")

name = "Rick"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.\n")

#Script 3:
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.\n")

#Script 4:
x = 2
y = 2
print(x == y)
print(x is y,"\n")

#Script 5:
print(not False) 
print((not False) == (False),"\n")

#Script 6:
# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

# do not change here
if number > 15:
    print("1")
if first_array:
    print("2")
if len(second_array) == 2:
    print("3")
if len(first_array) + len(second_array) == 5:
    print("4")
if first_array and first_array[0] == 1:
    print("5")
    print("\n\n")

#Script 7:
    print("Display the highest no. between the 3 inputs")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("enter the third numbre: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print ("The largest number is:" ,(largest))"""

#Script 8:
answer = (input("Are you sure you want to quit?(y/n): "))

    

if answer == 'Y':
    print ("Hope to see you again!!!")
elif answer == 'y':
    print ("Hope to see you again!!!")
elif answer == 'N':
    print ("Welcome back!!")
elif answer == 'n':
    print ("Welcome back!!")














