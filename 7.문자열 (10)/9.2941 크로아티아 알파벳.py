a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
cnt = 0

for i in a:
    cnt += b.count(i)
    b = b.replace(i, ' ')

b = b.replace(' ', '')
print(len(b) + cnt)