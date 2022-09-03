a = list(map(int, input().split()))
b = [1, 1, 2, 2, 2, 8]
c = ""

for i, j in zip(a, b):
    c += str(j - i) + " "

print(c)
