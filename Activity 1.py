def personal_details():
    Name = input("What is your Complete name: ")
    var_dept = input("What is your department: ")
    int_age = int(input("What is your age: "))
    address = input("What is your address :")
    print("My name is {} from {} dpartment".format(Name, var_dept))
    print("I'm {} years old and my address is {}.".format(int_age, address))

personal_details()
