l=int(input("enter length"))
b=int(input("enter breadth"))
area=l*b
peri=2*(l+b)
if area>peri:
    print(f"area {area} is greater than perimeter {peri}")
else:
    print(f"area {area} is less than perimeter {peri}")