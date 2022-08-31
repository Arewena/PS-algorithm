a = int(input())
b = a - 1

for i in range(a):
    print(' ' * b, end = '')
    print('*' * (a - b))
    b -= 1

