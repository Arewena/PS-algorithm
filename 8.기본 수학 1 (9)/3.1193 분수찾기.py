a = int(input())
b, c = 1, 1
while c + b <= a:
    c += b
    b += 1
d = a - c
e, f = d + 1, b - d
if not b % 2: print(f'{e}/{f}')
else: print(f'{f}/{e}')

#포기한 문제