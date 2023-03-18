from sys import stdin

n, m, v = list(map(int, stdin.readline().split()))
graph = {x+1: [] for x in range(n)}

for _ in range(m):
    node1, node2 = list(map(int, stdin.readline().split()))
    graph[node1].append(node2)
    graph[node2].append(node1)

for start in graph:
    graph[start].sort()

visited = []


def dfs(now):
    visited.append(now)
    for next in graph[now]:
        if next in visited:
            continue
        else:
            dfs(next)


dfs(v)
print(*visited, sep=' ')

visited = []
need_to_visit = [v]

while need_to_visit:
    now = need_to_visit.pop(0)
    if now in visited:
        continue
    visited.append(now)
    for next in graph[now]:
        if next in visited:
            continue
        else:
            need_to_visit.append(next)

print(*visited, sep=' ')
