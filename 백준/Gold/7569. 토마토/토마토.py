from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
tomato = []
q = deque()
for i in range(h):
    box = []
    for j in range(n):
        row = list(map(int, stdin.readline().split()))
        box.append(row)
        for k in range(m):
            if row[k] == 1:
                q.append((j, k, i))
    tomato.append(box)


directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
              (0, -1, 0), (0, 0, 1), (0, 0, -1)]
while q:
    now = q.popleft()
    for dir in directions:
        new_x, new_y, new_z = tuple(sum(elem) for elem in zip(now, dir))
        if 0 <= new_x < n and 0 <= new_y < m and 0 <= new_z < h and tomato[new_z][new_x][new_y] == 0:
            tomato[new_z][new_x][new_y] = tomato[now[2]][now[0]][now[1]] + 1
            q.append((new_x, new_y, new_z))
answer = 0
for z in tomato:
    for y in z:
        for x in y:
            if x == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(y))

print(answer-1)
