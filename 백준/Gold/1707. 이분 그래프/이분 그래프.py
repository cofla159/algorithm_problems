from sys import stdin
from collections import deque

k = int(stdin.readline().rstrip())
for _ in range(k):
    v, e = list(map(int, stdin.readline().split()))
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b = stdin.readline().split()
        a = int(a)
        b = int(b)
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    node = [0]*v

    def bfs(i):
        stack = deque()
        stack.append(i)
        while stack:
            now = stack.pop()
            if node[now] == 0:
                node[now] = 1
            for x in graph[now]:
                if node[x] == 0:
                    node[x] = -node[now]
                    stack.append(x)
                elif node[x] == node[now]:
                    return False
        return True

    answer = 'YES'
    for i in range(v):
        if node[i] == 0:
            result = bfs(i)
            if not result:
                answer = 'NO'
                break
    print(answer)
