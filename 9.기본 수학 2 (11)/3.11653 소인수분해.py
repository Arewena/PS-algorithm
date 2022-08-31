a = int(input())
b = []

while a != 1:
    for i in range(2, a + 1):
        if a % i == 0:
            a = a // i
            b.append(i)
            break

for i in sorted(b):
    print(i)