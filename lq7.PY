def ncr_npr():
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    f = math.factorial
    ncr = f(n) // (f(r) * f(n - r))
    npr = f(n) // f(n - r)
    print("nCr:", ncr)
    print("nPr:", npr)