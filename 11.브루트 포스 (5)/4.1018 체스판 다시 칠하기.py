a, b = map(int, input().split())
c = []
countList = []

for i in range(a):
    c.append(list(input().replace('', ' ').split()))

for i in range(a - 7):
    for j in range(b - 7):
        d = []
        count = 0
        for k in range(i, i + 8):
            d.append(c[k][0 + j:j + 8])

        p = ["W", "B", "W", "B", "W", "B", "W", "B"]
        for r in range(8):
            for w, z in zip(p, d[r]):
                if w != z:
                    count += 1
            p = list(reversed(p))
        countList.append(count)
        count = 0
        p = ["B", "W", "B", "W", "B", "W", "B", "W"]
        for r in range(8):
            for w, z in zip(p, d[r]):
                if w != z:
                    count += 1
            p = list(reversed(p))

        countList.append(count)
if countList:
    print(min(countList))
else:
    print(0)
