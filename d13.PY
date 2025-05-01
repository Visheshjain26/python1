def number_to_words():
    num = int(input("Enter a number between 0 and 19: "))
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
             "eighteen", "nineteen"]
    if 0 <= num <= 19:
        print("Word:", words[num])
    else:
        print("Invalid number. Please enter a number between 0 and 19.")
# number_to_words()