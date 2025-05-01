import random 
x=0
num=set()
for i in range(10):
    num.add(random.randint(15,45))
for i in list(num):
    if i<30:
        x=+1
    elif i>35:
        num.remove(i)
print(num)
print(x)


