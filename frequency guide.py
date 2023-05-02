user_input = input("Please Input a word: ")
count = [None] * len(user_input);  
   
for i in range(0, len(user_input)):  
    count[i] = 1;  
    for j in range(i+1, len(user_input)):  
        if(user_input[i] == user_input[j]):  
            count[i] = count[i] + 1;  
              
            #Set string[j] to 0 to avoid printing visited character  
            user_input = user_input[ : j] + '0' + user_input[j+1 : ];  
              
#Displays the each character and their corresponding frequency  
print("Characters and their corresponding frequencies");  
for i in range(0, len(count)):  
    if(user_input[i] != ' ' and user_input[i] != '0'):  
        print(user_input[i] + " - " + str(count[i]));

"""user_input = input("Please Input a word: ")

char_count = {}
  
for char in range(0,len(user_input)):
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1


print ("Count of all characters in user input:\n " + str(char_count))"""
