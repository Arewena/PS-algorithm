from math import ceil


for i in range(int(input())):
    a, b, c = map(int, input().split())
    if c % a == 0:
        d = str(a)
    else:
        d = str(c % a)

    if ceil(c / a) < 10:
        e = '0' + str(ceil(c / a))
    else:
        e = str(ceil(c / a))

    print(d + e)






