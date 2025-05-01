a=input("enter the string:")
count_alpha=0
count_num=0
for char in a:
    if char.isalpha():
        count_alpha+=1
    elif char.isdigit():
        count_num +=1
print(count_alpha)
print(count_num) 
print("the right fight")