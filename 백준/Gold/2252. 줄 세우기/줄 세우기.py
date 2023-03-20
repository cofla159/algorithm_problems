from sys import stdin
from collections import deque

n, m = list(map(int, stdin.readline().split()))
in_degree = [0]*n
queue = deque()
graph = [[] for _ in range(n)]
visited = []

for _ in range(m):
    smaller, taller = list(map(int, stdin.readline().split()))
    graph[smaller-1].append(taller)
    in_degree[taller-1] += 1

for i, x in enumerate(in_degree):
    if x == 0:
        queue.append(i+1)
        in_degree[i] = -1

while queue:
    node = queue.popleft()
    visited.append(node)
    for taller in graph[node-1]:
        in_degree[taller-1] -= 1
        if in_degree[taller-1] == 0:
            queue.append(taller)
            in_degree[taller-1] -= 1
    # for i, x in enumerate(in_degree):
    #     if x == 0:
    #         queue.append(i+1)
    #         in_degree[i] = -1


print(*visited, sep=' ')
