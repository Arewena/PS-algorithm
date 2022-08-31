while(True):
    a = list(map(int, input().split()))
    if sum(a) == 0:
        break

    big = max(a) ** 2
    a.remove(max(a))
    small = sum((min(a) ** 2, max(a) ** 2))

    if big == small:
        print('right')

    else:
        print('wrong')