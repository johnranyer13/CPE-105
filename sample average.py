print("Enter the Value of n: ", end="")
n = int(input())
print("Enter " +str(n)+ " Numbers: ", end="")
arr = []
for i in range(n):
    arr.append(int(input()))

sum = 0
for i in range(n):
    sum = sum+arr[i]
    if i==0:
        print(end="\n(" +str(arr[i]))
    elif i==(n-1):
        print(end="+" +str(arr[i])+ ")")
    else:
        print(end="+" +str(arr[i]))

print(end="/" +str(n)+ " = ")
avg = sum/n
print(end=str(avg))
print()
