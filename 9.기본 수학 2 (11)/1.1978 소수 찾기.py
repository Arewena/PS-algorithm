input()
a = list(map(int, input().split()))
boolean = True
count = 0

for i in a:
    boolean = True
    if i > 1:
        for j in range(2, i + 1):
            if i % j == 0 and i != j:
                boolean = False
                break
        if boolean: count += 1
print(count)