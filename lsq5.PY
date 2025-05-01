def convert_uppercase():
    words = ["hello", "world", "python", "list", "string"]
    print("Original list of strings:", words)
    upper_words = [i.upper() for i in words]
    print("List with uppercase strings:", upper_words)