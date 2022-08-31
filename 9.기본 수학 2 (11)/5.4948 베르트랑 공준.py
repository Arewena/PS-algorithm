while True:
    a = int(input()) * 2
    if a == 0: break
    b = [True] * a
    c = int(a ** 0.5)

    for i in range(2, c + 1):
        if b[i]:
            for j in range(i + i, a, i):
                b[j] = False
    if a == 2:
        print(1)
    else:
        print(len(list(filter(lambda x: a >= x > (a // 2), [i for i in range(1, a) if b[i]]))))

#포기한 문제