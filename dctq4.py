str = input("Enter a string: ")

charfreq = {}
for char in str:
    if char in charfreq:
        charfreq[char] += 1
    else:
        charfreq[char] = 1

print("Character Frequency ", charfreq)
