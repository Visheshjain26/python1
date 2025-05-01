x1, y1 = 1, 2
x2, y2 = 3, 4
x3, y3 = 5, 6

if (x2 - x1 == 0 or x3 - x2 == 0 or x3 - x1 == 0):
    print("Vertical line detected; checking slopes")
    if (x2 - x1 == 0 and x3 - x2 == 0 and x3 - x1 == 0):
        print("The points are lying on a straight line")
    else:
        print("The points are not lying on a straight line")
else:
    
    slope1 = (y2 - y1) / (x2 - x1)
    slope2 = (y3 - y2) / (x3 - x2)
    slope3 = (y3 - y1) / (x3 - x1)

    if slope1 == slope2 == slope3:
        print("The points are lying on a straight line")
    else:
        print("The points are not lying on a straight line")
