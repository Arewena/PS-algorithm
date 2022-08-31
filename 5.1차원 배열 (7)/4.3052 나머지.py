a = list(map(int, [input() for _ in range(10)]))
for i in a:
    a[a.index(i)] = i % 42

print(len(set(a)))
