from sys import stdin

n = int(stdin.readline().rstrip())
connected = []

visited = [False]*n
parent = [None]*n
graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = list(map(int, stdin.readline().split()))
    graph[a-1].append(b)
    graph[b-1].append(a)

stack = [1]
while stack:
    root = stack.pop()
    visited[root-1] = True
    for i in graph[root-1]:
        if visited[i-1]:
            continue
        parent[i-1] = root
        stack.append(i)

for i in parent:
    if i == None:
        continue
    else:
        print(i)
