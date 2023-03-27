from sys import stdin

n = int(stdin.readline())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, stdin.readline().split())))

memo = [[None]*n for _ in range(n)]
for i in range(n):  # i번째 대각선
    for j in range(n-i):  # 대각선에서 몇 번째
        if i == 0:
            memo[j][j] = 0
        elif i == 1:
            memo[j][j+1] = matrix[j][0]*matrix[j][1]*matrix[j+1][1]
        else:
            possibles = []
            for k in range(i):  # 어디서 끊는지
                possibles.append(memo[j][j+k]+memo[k+j+1][j+i] +
                                 matrix[j][0]*matrix[j+k][1]*matrix[i+j][1])
            memo[j][j+i] = min(possibles)
print(memo[0][n-1])
