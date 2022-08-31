a = int(input())
A = 0
B = 1

if a == 0:
    print(0)

elif a == 1:
    print(1)
else:
    for i in range(3, a + 1):
        if i % 2 == 1:
            A = A + B
        else:
            B = B + A

    print(A + B)