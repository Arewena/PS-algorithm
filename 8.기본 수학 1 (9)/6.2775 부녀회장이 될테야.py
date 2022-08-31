room = []
a = []


for i in range(int(input())):
    room = []
    cnt = 1
    k = int(input())
    n = int(input())

    for j in range(1, n + 1): room.append(j)

    for floor in range(k):
        for l in range(1, n + 1):
            q = 0
            for p in range(0, l): q += room[p]
            a.append(q)
        room = a
        a = []

    print(room[-1])


#포기한 문제