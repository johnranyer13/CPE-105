print("----------------------------------")
print("|       Please Input a word      |")
print("----------------------------------")
user_input = input("-->")

count = [None] * len(user_input);  
   
for i in range(0, len(user_input)):  
    count[i] = 1;  
    for j in range(i+1, len(user_input)):  
        if(user_input[i] == user_input[j]):  
            count[i] = count[i] + 1;
            
            user_input = user_input[ : j] + '0' + user_input[j+1 : ];
            
print("----------------------------------")               
print("Frequency of each charcter: ");  
for char in range(0, len(count)):  
    if(user_input[char] != ' ' and user_input[char] != '0'):  
        print(user_input[char] + " - " + str(count[char]));
print("----------------------------------")
