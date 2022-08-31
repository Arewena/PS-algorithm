for i in range(int(input())):
    a, b = input().split()
    a = int(a)

    for i in b:
        print(i * a, end = '')

    print()