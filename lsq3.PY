def remove_duplicates():
    nums = [random.randint(1, 30) for i in range(50)]
    print("Original list with duplicates:", nums)
    unique_nums = list(set(nums))
    print("List after removing duplicates:", unique_nums)