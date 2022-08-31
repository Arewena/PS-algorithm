a = list(map(int, [input() for _ in range(9)]))

print("{0}\n{1}".format(max(a), a.index(max(a)) + 1))