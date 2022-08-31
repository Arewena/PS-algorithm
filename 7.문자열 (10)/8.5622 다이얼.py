a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
b = input()
c = 0

for i in b:
    for j in a:
        if i in j:
            c += int(a.index(j)) + 3

print(c)