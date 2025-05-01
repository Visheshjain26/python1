def find_occurance():
    num = [random.randint(1, 50) for i in range(20)]
    print("list of 20 random numbers:", num)
    n = int(input("Enter number to find occurrences: "))
    ans = []
    for i in range(20):
        if num[i] == n:
            ans.append(i)
    print("The number occurs at:", ans)