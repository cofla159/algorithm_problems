from sys import stdin
import math
INF = float('inf')

n, m = map(int, stdin.readline().split())
small = []
for _ in range(m):
    small.append(int(stdin.readline()))

small.sort()

max_jump = math.floor((2*n)**(1/2))  # 최대 속도
jump = [[INF]*(max_jump+1) for _ in range(n+1)]
jump[1][0] = 0
for i in range(2, n+1):
    if i in small:
        continue
    for j in range(1, math.floor((2*i)**(1/2))+1):
        jump[i][j] = min(jump[i-j][j], jump[i-j][j+1], jump[i-j][j-1]) + \
            1 if j+1 <= max_jump else min(jump[i-j][j], jump[i-j][j-1])+1

print(min(jump[n]) if min(jump[n]) != INF else -1)
