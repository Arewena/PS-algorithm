a, b = 1, 1
c = []

while a != '0' and b != '0':
    a, b = map(str, input().split())

    if a == '0' and b == '0':
        continue

    else:
        c.append(map(int, (a, b)))

for i in c:
    print(sum(i))