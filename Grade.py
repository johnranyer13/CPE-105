def student_grades():
    print ("-----------------------------------")
    print ("|    Please Enter Your Grades     |")
    print ("-----------------------------------\n")

# Get the user score for each quiz
# Get the total average of all quizes
    print ("-----------------------------------")
    print ("Each quiz total of 100 items")
    print ("Enter Marks of Quiz :")
    Quiz1 = float(input("Quiz 1 :"))
    Quiz2 = float(input("Quiz 2 :"))
    Quiz3 = float(input("Quiz 3 :"))
    Quiz_Avg = 100 * (Quiz1 + Quiz2 + Quiz3) / 300
    print ("-----------------------------------")
    print ("|   Average of Quiz is : ",(Quiz_Avg),"  |")
    print ("-----------------------------------\n")

# Get the user score for each project
# Get the total average of all prejects
    print ("-----------------------------------")
    print ("Each project total of 100 score")
    print ("Enter Marks of Project :")
    Project1 = float(input("Project 1 :"))
    Project2 = float(input("Project 2 :"))
    Project3 = float(input("Project 3 :"))
    Proj_Avg = 100 * (Project1 + Project2 + Project3) / 300
    print ("-----------------------------------")
    print ("|  Average of Project is : ",(Proj_Avg),"|")
    print ("-----------------------------------\n")

# Get the user score for final exam
# Get the total average of final exam
    print ("-------------------------------------")
    print ("Final Exam total of 100 score")
    print ("Enter Mark of Final Exam: ")
    Finalexam = float(input("Your Score : "))
    Final_Avg = 100 * (Finalexam) / 100
    print ("-------------------------------------")
    print ("| Average of Final Exam is : ",(Final_Avg),"|")
    print ("-------------------------------------\n")

# Get the user score for assignment
# Get the total average of assignment
    print ("-------------------------------------")
    print ("Assingment total of 100 items")
    print ("Enter Mark of Assignment: ")
    Assignment = float(input("Your Score : "))
    Assign_Avg = 100 * (Assignment) / 100
    print ("-------------------------------------")
    print ("| Average of Assignment is : ",(Assign_Avg),"|")
    print ("-------------------------------------\n")

# Get the user score for class standing
# Get the total average of class standing
    print ("-----------------------------------------")
    print ("Class Standing total of 100 score")
    print ("Enter Mark of Class Standing: ")
    Class_Sta = float(input("Your Score : "))
    Class_Sta_Avg = 100 * (Class_Sta) / 100
    print ("-----------------------------------------")
    print ("| Average of Class Standing is : ",(Class_Sta_Avg),"|")
    print ("-----------------------------------------\n")


# Get the total average score of the course
    Total_Avg = (Quiz_Avg * 30 / 100) + (Proj_Avg * 20 / 100) + (Finalexam * 30 / 100) + (Assignment * 10/100) + (Class_Sta * 10/100)
    print ("---------------------------------------")
    print ("| Average Score of Course is : ",(Total_Avg),"|")
    print ("---------------------------------------\n")

student_grades()
