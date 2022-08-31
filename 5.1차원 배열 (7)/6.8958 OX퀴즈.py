count = 0
score = 0

for i in range(int(input())):
    a = input()

    for j in a:
        if j == 'O':
            count += 1
            score += count

        else:
            count = 0

    print(score)
    score = 0
    count = 0

#포기한 문제