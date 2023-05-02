"""#Script 1:
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)"""

"""#Script 2:
for x in range(5):
    print(x)

for x in range(3, 6):
    print(x)

for x in range(3, 8, 2):
    print(x)"""

"""#Script 3:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
        # loop fell through without finding a factor
            print(n, 'is a prime number')"""

"""#Script 4:
for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)"""

"""#Script 5:
count = 0
while count < 60:
   	print(count)
   	continue
count += 10"""

"""#Script 6:
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):
# Check if x is even
    if x % 2 == 0:
        continue
    print(x)"""

"""#Script 7:
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)"""

#Scrip 8:
count = 20

while (count <= 200):
    print (count)
    count = count + 30
print ("BOOOOOM!!!")


