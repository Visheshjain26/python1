lst = ['madam','Python',"malayalam","12321"]
def palindrome(x):
    return x==x[::-1]
print(list(filter(palindrome,lst)))