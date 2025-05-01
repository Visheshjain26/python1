import random
ls=[]
for i in range(0,10):
    ls.append([random.randint(-15,15)])
print(list(map(lambda x : x*x,ls)))


