from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n)]
for _ in range(m):
    start, end, path_cost = tuple(map(int, stdin.readline().split()))
    graph[start-1].append((end-1, path_cost))
start, dest = stdin.readline().split()
start = int(start)-1
dest = int(dest)-1

min_cost = [10**10]*n
pq = []
heapq.heappush(pq, (0, start))
while pq:
    (now_cost, now_node) = heapq.heappop(pq)
    if now_node == dest:
        print(now_cost)
        break
    if min_cost[now_node] < now_cost:
        continue
    for x_node, x_cost in graph[now_node]:
        next_cost = now_cost+x_cost
        if next_cost < min_cost[x_node]:
            min_cost[x_node] = next_cost
            heapq.heappush(pq, (min_cost[x_node], x_node))
