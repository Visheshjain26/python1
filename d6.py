num=int(input("enter number"))
temp=num
count=0
while temp!=0:
    count=count +1
    temp//=10

print("the no. of digits are ",count)
