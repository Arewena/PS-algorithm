a = int(input())
b = input()


print(a * int(b[-1]))
print(a * int(b[-2]))
print(a * int(b[-3]))
print((a * int(b[-1]) + a * int(b[-2] + '0') + a * int(b[-3] + '00')))
