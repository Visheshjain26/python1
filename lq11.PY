def sin_x():
    deg = float(input("Enter angle in degrees: "))
    x = deg * 3.14159 / 180
    term = x
    sinx = 0
    sign = 1
    for i in range(1, 10, 2):
        sinx += sign * term
        sign *= -1
        term *= x * x / ((i + 1) * (i + 2))
    print("sin(x) approx:", sinx)