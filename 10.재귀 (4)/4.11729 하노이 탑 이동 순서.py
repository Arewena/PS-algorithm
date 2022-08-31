import sys

sys.setrecursionlimit(100000)
a = []
b = []


def hanoi(number_of_disks_to_move, from_, to_, via_):
    if number_of_disks_to_move == 1:
        a.append(from_)
        b.append(to_)
    else:
        hanoi(number_of_disks_to_move - 1, from_, via_, to_)
        a.append(from_)
        b.append(to_)
        hanoi(number_of_disks_to_move - 1, via_, to_, from_)


hanoi(int(input()), 1, 3, 2)
print(len(a))
for i in range(len(a)):
    print(a[i], b[i])

#퍼온 문제