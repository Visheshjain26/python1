f_name = ["Aarav", "Priya", "Vihaan", "Ananya", "Rohan"]

def length_name(x):
    return len(x) > 8  

print(list(filter(length_name, f_name)))
