a = []
b = []

for i in range(3):
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)


for i, j in zip(a, b):
    if a.count(i) == 1:
        c = i

    if b.count(j) == 1:
        d = j

print(c, d)
