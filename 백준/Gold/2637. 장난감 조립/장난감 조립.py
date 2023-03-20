from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())
parts = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)
degree[0] = -100
queue = deque()

for _ in range(m):
    x, y, k = list(map(int, stdin.readline().split()))
    degree[x] += 1
    if not graph[y]:
        graph[y] = []
    graph[y].append(x)
    if not parts[x]:
        parts[x] = []
    parts[x].append((y, k))

for i, x in enumerate(degree):
    if x == 0:
        queue.append(i)


def get_basic_parts_num(dest):
    if not parts[dest]:
        return {dest: 1}
    answer = {}
    for basic, num in parts[dest]:
        for k, v in parts[basic].items():
            if answer.get(k):
                answer[k] += v*num
            else:
                answer[k] = v*num
    return answer


while queue:
    now = queue.popleft()
    parts[now] = get_basic_parts_num(now)
    for x in graph[now]:
        degree[x] -= 1
        if degree[x] == 0:
            queue.append(x)

answer = []
for k, v in parts[n].items():
    answer.append((k, v))

answer.sort()

for x in answer:
    print(f'{x[0]} {x[1]}')
