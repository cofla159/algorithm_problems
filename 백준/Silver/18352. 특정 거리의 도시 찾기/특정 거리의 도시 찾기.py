from sys import stdin
from collections import deque

n, m, k, x = list(map(int, stdin.readline().split()))
graph = {}
for _ in range(m):
    a, b = list(map(int, stdin.readline().split()))
    if not graph.get(a):
        graph[a] = []
    graph[a].append(b)


need_visit = deque()
visited = [False]*n
need_visit.append([x, 0])
visited[x-1] = True
answer = []

while need_visit:
    start, cost = need_visit.popleft()
    if cost == k:
        answer.append(start)
        continue
    # if not False in visited:
    #     answer.append(-1)
    #     break
    if graph.get(start) and cost + 1 <= k:
        for end in graph[start]:
            if not visited[end-1]:
                need_visit.append([end, cost+1])
                visited[end-1] = True
if len(answer) > 0:
    print(*sorted(answer), sep='\n')
else:
    print(-1)
