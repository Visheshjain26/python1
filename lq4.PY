def number_checks():
    n = int(input("Enter a number: "))
    prime = all(n%i!=0 for i in range(2, int(n**0.5)+1)) and n > 1
    perfect = sum(i for i in range(1, n) if n%i==0) == n
    armstrong = sum(int(i)**len(str(n)) for i in str(n)) == n
    palindrome = str(n) == str(n)[::-1]
    square = n*n
    automorphic = str(square).endswith(str(n))
    print("Prime:", prime)
    print("Perfect:", perfect)
    print("Armstrong:", armstrong)
    print("Palindrome:", palindrome)
    print("Automorphic:", automorphic)