from sys import stdin
import sys
sys.setrecursionlimit(10**7)

n = int(stdin.readline())
trees = []
for _ in range(n):
    trees.append(list(map(int, stdin.readline().split())))

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
memo = [[None]*n for _ in range(n)]


def dfs(x, y):
    if memo[x][y] != None:
        return memo[x][y]
    memo[x][y] = 0
    for i, j in directions:
        if 0 <= x+i <= n-1 and 0 <= y+j <= n-1 and trees[x][y] < trees[x+i][y+j]:
            memo[x][y] = max(memo[x][y], dfs(x+i, y+j))
    memo[x][y] +=1
    return memo[x][y]


answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)
