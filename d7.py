year=int(input("entter year: "))
if year<=0:
    print("enter valid year")
elif year%4==0:
    print("it is a leap year")
else:
    print("it is not leap year")