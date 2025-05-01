vowels='aeiou'
input_string=input("please enter a string:")
count=0
for char in input_string:
    if char in vowels:
        count+=1
print("number of vowels in string:",count)