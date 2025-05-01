def list_diff():
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [2, 4, 6, 8]
    result = [i for i in list1 if i not in list2]
    print("List1:", list1)
    print("List2:", list2)
    print("Elements in List1 but not in List2:", result)