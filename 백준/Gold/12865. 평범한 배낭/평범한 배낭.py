from sys import stdin

n, k = map(int, stdin.readline().split())
things = []
for _ in range(n):
    things.append(tuple(map(int, stdin.readline().split())))

result = [[0]*(k+1) for _ in range(n)]

for i in range(1, k+1):
    if i >= things[0][0]:
        result[0][i] = things[0][1]
for i in range(n):
    result[i][0] = 0

for i in range(1, n):
    now_w, now_v = things[i]
    for j in range(1, k+1):
        if j >= now_w:
            result[i][j] = max(result[i-1][j-now_w] + now_v, result[i-1][j])
        else:
            result[i][j] = result[i-1][j]

print(result[n-1][k])
