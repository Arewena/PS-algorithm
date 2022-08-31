a = int(input()); b = int(input()); c = int(input())
a = str(a * b * c)
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in a:
    num.append(int(i))

for i in range(0, 10):
    print(num.count(i) - 1)
