a = int(input())
b = []

for i in range(a):
    b.append(list(map(int, input().split())))

for i in b:
    print(sum(i))