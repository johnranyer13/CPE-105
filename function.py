#Practice
#function:
"""def printme(str):
    "this prints a passed string into this function"
    print(str)
    return;

printme(str = "My string")"""

"""def printinfo(name, age):
    "this prints a passed info into this function"
    print ("Name: ", name)
    print ("Age: ", age)
    return;

printinfo(age=50, name="miki")"""

#default arguments:
"""def printinfo(name, age = 35):
    "this prints a passed info into this function"
    print ("Name: ", name)
    print ("Age: ", age)
    return;


printinfo(age=50, name="miki")
printinfo(name="miki")"""

#non-keyword variable argument:
"""def printinfo(arg1, *vartuple):
    print(arg1)
    for var in vartuple:
        print(var)
    return

print("Output is")
printinfo(10)
printinfo(70, 60, 50)"""

#Anonymus Functions
"""sum = lambda num1, num2: num1 + num2;

print("Value of total : ",sum(10,20))
print("Value of total : ",sum(20,20))"""

#Anonymus Functions
def sum(num1, num2):
    total = num1 + num2
    print("Inside the Function : ",(total))
    return total

total = sum(10,20)
print("Outside the function : ",(total))
