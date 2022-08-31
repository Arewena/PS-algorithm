for i in range(int(input())):
    a = list(map(int, input().split()))
    c = []
    d = a[0]
    a.remove(a[0])
    b = sum(a) / len(a)
    for j in a:
        if j > b:
            c.append(j)

    print("{:.3f}%".format(100 / d * len(c)))