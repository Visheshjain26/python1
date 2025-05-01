x = int(input("enter the value of x: "))
y = int(input("enter the value of y: "))
z = int(input("enter the value of z: "))

# Finding the greatest and smallest numbers in one structure
if x > y and x > z:
    print("x is the greatest no.")
    print("z is the smallest no." if y > z else "y is the smallest no.")
elif y > x and y > z:
    print("y is the greatest no.")
    print("z is the smallest no." if x > z else "x is the smallest no.")
else:
    print("z is the greatest no.")
    print("y is the smallest no." if x > y else "x is the smallest no.")
