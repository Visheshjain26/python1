def split_pos_neg():
    nums = [random.randint(-50, 50) for i in range(30)]
    print("Original list of 30 numbers:", nums)
    positives = [i for i in nums if i > 0]
    negatives = [i for i in nums if i < 0]
    print("Positive numbers:", positives)
    print("Negative numbers:", negatives)