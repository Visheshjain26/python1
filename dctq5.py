prices = {
    "rice": 50,
    "wheat": 30,
    "milk": 20,
    "sugar": 40
}

quantities = {
    "rice": 2,
    "wheat": 3,
    "milk": 5,
    "sugar": 1
}

total_bill = 0
for item in prices:
    if item in quantities:
        total_bill += prices[item] * quantities[item]

print("Total Grocery Bill: Rs.", total_bill)
