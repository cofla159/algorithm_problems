from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n)]
degree = [0]*n
q = deque()

for _ in range(m):
    start, end, time = list(map(int, stdin.readline().split()))
    graph[start-1].append((end-1, time))
    degree[end-1] += 1
start_node, end_node = stdin.readline().split()
start_node = int(start_node) - 1
end_node = int(end_node) - 1

for i in range(n):
    if degree[i] == 0:
        q.append(i)

max_time = [-1]*n
max_time[start_node] = 0
roads = [[] for _ in range(n)]
while q:
    current_node = q.popleft()
    for linked_node, taken_time in graph[current_node]:
        degree[linked_node] -= 1
        if degree[linked_node] == 0:
            q.append(linked_node)
        if max_time[linked_node] < max_time[current_node]+taken_time:
            max_time[linked_node] = max_time[current_node]+taken_time
            roads[linked_node] = [current_node]
        elif max_time[linked_node] == max_time[current_node]+taken_time:
            roads[linked_node].append(current_node)
print(max_time[end_node])


q.clear()
q.append(end_node)
running_roads = set()
visited = [[False for _ in range(n)]
           for _ in range(n)]  # [x][y] : x->y 길을 방문했는지
while q:
    current_node = q.popleft()
    for next_node in roads[current_node]:
        if not visited[current_node][next_node]:
            running_roads.add((current_node, next_node))
            q.append(next_node)
            visited[current_node][next_node] = True


print(len(running_roads))
