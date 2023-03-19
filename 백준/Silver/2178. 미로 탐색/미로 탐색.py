from sys import stdin
from collections import deque

n, m = list(map(int, stdin.readline().split()))
maze = [[int(x) for x in stdin.readline().rstrip()] for _ in range(n)]
count = 0
need_visit = deque()
need_visit.append([(0, 0), 1])
visited = [[False]*m for _ in range(n)]

while need_visit:
    (x, y), count = need_visit.popleft()
    if (x, y) == (n-1, m-1):
        print(count)
        break
    if y != 0 and maze[x][y-1] != 0 and not visited[x][y-1]:  # 왼
        need_visit.append([(x, y-1), count+1])
        visited[x][y-1] = True
    if y != m-1 and maze[x][y+1] != 0 and not visited[x][y+1]:  # 오
        need_visit.append([(x, y+1), count+1])
        visited[x][y+1] = True
    if x != 0 and maze[x-1][y] != 0 and not visited[x-1][y]:  # 위
        need_visit.append([(x-1, y), count+1])
        visited[x-1][y] = True
    if x != n-1 and maze[x+1][y] != 0 and not visited[x+1][y]:  # 아래
        need_visit.append([(x+1, y), count+1])
        visited[x+1][y] = True
