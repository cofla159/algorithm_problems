from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = stdin.readline().split()
    a = int(a)
    b = int(b)
    graph[a].append(b)
    back_graph[b].append(a)


def dfs(start, graph):
    stack = [start]
    visited = [False]*(n+1)
    visited[start] = True
    while stack:
        now = stack.pop()
        for next in graph[now]:
            if not visited[next]:
                stack.append(next)
                visited[next] = True

    return visited.count(True)-1


cnt = 0
for i in range(1, n+1):
    if dfs(i, graph) > n//2 or dfs(i, back_graph) > n//2:
        cnt += 1

print(cnt)
