g=float(input("enter the value of gross salary"))
a=0.1*g
d=0.03*g
f=g+a-d
print("the net salary is:",f)
g=float(input("enter the value of gross sale"))
d=0.1*g
n=g-d
print("the net sales is:",n)
a=int(input("enter the first subject marks"))
b=int(input("enter the second subject marks"))
c=int(input("enter the third subject marks"))
d=(a+b+c)/3
print("the average of three subjects is:",d)
a=int(input("enter the  value of a"))
b=int(input("enter the  value of b"))
a,b=b,a
print("a=",a)
print("b=",b)