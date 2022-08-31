cnt = 0
for i in range(int(input())):
    a = input()
    b = []
    c = True

    for j in a:
        if a.count(j) >= 2:
            b = [index for index, value in  enumerate(a) if value == j]
            if max(b) - a.count(j) + 1 > min(b):
                c = False
                break
    if c == True:
         cnt += 1

print(cnt)

#포기한 문제