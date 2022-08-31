a = int(input())
b = 0

while a > 0:
    if a == 0:
        break
    b += 1
    if "666" in str(b):
        a -= 1

print(b)