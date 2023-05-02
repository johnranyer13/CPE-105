def list_benefits():
    each_benefits = ["More organized code", "More readable code",
                "Easier code reuse",
                "Allowing programmers to share and connect code together"]
    return each_benefits

def build_sentence(food):
    return food + " is good for your health!"

def final_builder():
    all_benefits = list_benefits()
    for food in all_benefits:
        print (build_sentence(food))

def mean_num():
    print("Enter the how many value: ")
    n = int(input())
    print("Enter " +str(n)+ " Numbers: ")
    nums = []
    for i in range(n):
        nums.insert(i, int(input()))

    sum = 0
    for i in range(n):
        sum = sum+nums[i]

    mean = sum/n
    print("\nMean = ", mean)


final_builder()
mean_num()
