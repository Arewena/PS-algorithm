input()
a = list(map(int, input().split()))
b = []

for i in a:
    b.append(i / max(a) * 100)

print(sum(b) / len(b))