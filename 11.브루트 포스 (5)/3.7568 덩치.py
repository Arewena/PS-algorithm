a = []
b = []
for i in range(int(input())):
    a.append(list(map(int, input().split())))

for i in a:
    c = 0

    for j in a:
        if i[0] < j[0] and i[1] < j[1]:
            c += 1
    b.append(c + 1)

for i in b:
    print(i, end=' ')