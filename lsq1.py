import random
odd_num=[1,3,5,9,7]
even_num=[2,4,6,8]
print(odd_num)
print(even_num)
odd_num[2]=even_num
print(odd_num)
print(even_num)
new_list=sum(odd_num,[])
sorted_list=sorted(new_list)
print(sorted_list)