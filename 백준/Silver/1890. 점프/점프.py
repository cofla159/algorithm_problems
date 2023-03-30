from sys import stdin

n = int(stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

memo = [[0]*n for _ in range(n)]
memo[0][0] = 1

for i in range(n):
    for j in range(n):
        new_right = j+board[i][j]
        new_down = i+board[i][j]
        if not (i == n-1 and j == n-1):
            if new_right <= n-1:
                memo[i][new_right] += memo[i][j]
            if new_down <= n-1:
                memo[new_down][j] += memo[i][j]

print(memo[n-1][n-1])
