from math import sqrt, pow
def check_point_in_circle():
    x, y = map(int, input("Enter coordinates of point (x, y): ").split())
    h, k = map(int, input("Enter coordinates of center of circle (h, k): ").split())
    r = float(input("Enter radius of the circle: "))
    distance = sqrt(pow(x - h, 2) + pow(y - k, 2))
    if distance < r:
        print("Point lies inside the circle")
    elif distance == r:
        print("Point lies on the circle")
    else:
        print("Point lies outside the circle")