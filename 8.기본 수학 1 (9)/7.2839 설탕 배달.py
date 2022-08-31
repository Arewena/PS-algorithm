number = int(input())
five = 5 * (number // 5)
count = five // 5

while five != number:
    if five + 3 <= number:
        five += 3
        count += 1
    else:
        five -= 5
        count -= 1

    if five < 3:
        if five == 0:
            five += 3
            count += 1
        else:
            count = -1
            break

print(count)
