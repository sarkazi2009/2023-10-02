for k in range(3, 21):
    code = str(str(k)+'-')
    for i in range(1, k):
        for j in range(i + 1, k):
            if k % (i + j) == 0:
                code = code + str(i) + str(j)
    print(code)
