a, b = map(int, input().split())

if b - 45 < 0:
    b += 60 - 45
    a -= 1
else:
    b -= 45
if a < 0:
    a = 23
print(a, b)
