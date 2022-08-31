a, b = map(int, input().split())
c = list(map(int, input().split()))
maxinum = 0

for i in c:
    for j in c:
        for k in c:
            if b >= i + j + k > maxinum and i != j != k and i != k:
                maxinum = i + j + k

print(maxinum)