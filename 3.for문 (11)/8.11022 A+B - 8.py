a = int(input())
b = []
c = 1

for i in range(a):
    b.append(list(map(int, input().split())))


for i in b:
    print("Case #{0}: {1} + {2} = {3}".format(c, i[0], i[1], sum(i)))
    c += 1

