a = int(input())
b = int(input())
c = []

for i in range(a, b + 1):
    if i != 1:
        d = True
        for j in range(2, i):
            if i % j == 0:
                d = False
                break
        if d == True:
            c.append(i)

if c == []:
    print(-1)
else:
    print(sum(c))
    print(min(c))

