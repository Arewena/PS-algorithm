a = input()
b = 0
c = 0

for i in range(1, int(a)):
    b = i
    c = 0
    for j in str(i):
        c += int(j)

    if b + c == int(a):
        print(b)
        break


if b + c != int(a):
    print(0)