a = []
for i in range(1, 10001):
    b = 0
    if i not in a:
        b += i
        for j in str(i):
            b += int(j)
        a.append(b)
        print(i)
    else:
        b += i
        for j in str(i):
            b += int(j)
        a.append(b)
