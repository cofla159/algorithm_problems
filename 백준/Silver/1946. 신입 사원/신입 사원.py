from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    score = []
    for _ in range(n):
        score.append(list(map(int, stdin.readline().split())))

    score.sort()
    cnt = 1
    last_rank = score[0][1]
    for i in range(1, n):
        if last_rank > score[i][1]:
            cnt += 1
            last_rank = score[i][1]

    print(cnt)
