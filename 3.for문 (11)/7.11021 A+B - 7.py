a = int(input())
b, c = 0, 0
d = []
count = 1

for i in range(a):
    b, c = map(str, input().split())
    d.append(map(int, b + c))


for i in d:
    print("Case #{0}: {1}".format(count, sum(i)))
    count += 1
