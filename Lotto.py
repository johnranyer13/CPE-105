import random
lotto_nums = []
winning_nums = []
counter = 1

print ("------------------------------------------------")
print ("|           Welcome to LOTTO 6/42              |")
print ("------------------------------------------------")
print ("\n------------------------------------------------")
print ("|     Enter your 6 numbers between 1 and 42    |")
print ("------------------------------------------------")


for i in range (0,6):
  number = random.randint(1,42)
  while number in winning_nums:
    number = random.randint(1,42)
  winning_nums.append(number)

winning_nums.sort()

while counter <=6:
    print ("Please type in the", (counter),"number")
    i = int(input("--> "))
    if (i not in lotto_nums) and (1 <= i <= 42) and type(i) == type(7):
            lotto_nums.append(i)
            counter = counter + 1
            
    else:
        print ("Please enter a number between 1 and 42!")

    
print ("------------------------------------------------------------")
print ("| The nummbers you have chosen are:", (lotto_nums), "|")
print ("------------------------------------------------------------")
print ("\n----------------------------------------------------------")
print ("|    The winning numbers are:", (winning_nums),    "    |")
print ("----------------------------------------------------------\n")

n = 0
for i in lotto_nums:
    if i in winning_nums:
        n += 1
print ("----------------------------------------------------------")
print ("You got %d numbers right out of 6" % n)
if n < 3:
    print ("Try Again Next Time!!")
elif n == 3:
    print ("Congratulations!!! You have won ₱20 and balik taya")
elif n == 4:
    print ("Congratulations!!! You have won ₱1000")
elif n == 5:
    print ("Congratulations!!! You have won ₱25000")
elif n == 6:
    print ("Congratulations!!! You have won the JACKPOT!!!")
print ("----------------------------------------------------------")
            
