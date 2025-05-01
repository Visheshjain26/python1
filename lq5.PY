def pythagorean_triplets():
    for i in range(1, 31):
        for j in range(i, 31):
            k = int((i*2 + j2)*0.5)
            if k <= 30 and i*2 + j2 == k*2:
                print(i, j, k)