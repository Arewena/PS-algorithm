for i in range(int(input())):
    a = int(input())
    b = [True] * a
    c = int(a ** 0.5)
    for i in range(2, c + 1):
        if b[i]:
            for j in range(i + i, a, i):
              b[j] = False
    d = [i for i in range(2, a) if b[i]]
    e = [10000, 5000, 0]
    for i in d:
        for j in d:
            if i + j == a and max(e[0], e[1]) - min(e[0], e[1]) > max(i, j) - min(i, j):
                e = [i, j, i + j]
    print(e[0], e[1])

#포기한 문제
