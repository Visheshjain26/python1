names = {"aarav", "Ananya", "amit", "Bhavya", "bharat", "aisha"}

a_names = set()
b_names = set()

for name in names:
    if name.lower().startswith("a"):
        a_names.add(name)
    elif name.lower().startswith("b"):
        b_names.add(name)

print("Names starting with A:", a_names)
print("Names starting with B:", b_names)
