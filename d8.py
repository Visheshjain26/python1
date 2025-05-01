a1=int(input("enter the first angle of triangle"))
a2=int(input("enter the second angle of triangle"))
a3=int(input("enter the third angle of triangle"))

if a1<0 or a2<0 or a3<0 :
    print("enter valid angle")
elif a1+a2+a3==180:
    print("it is a triangle")
else:
    print("it is not a triangle")
