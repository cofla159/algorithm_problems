from sys import stdin
from collections import deque
n = int(stdin.readline())
memo = [[0]*(2**n) for _ in range(n+1)]
graph = []
for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))

q = deque()
q.append((1, 1))

while q:
    now, visited = q.popleft()  # now, next 둘다 도시번호 그대로(1부터 시작)
    for next in range(1, n+1):
        if graph[now-1][next-1] == 0:
            continue
        if len(bin(visited & (1 << (next-1)))) < next+2 or bin(visited & (1 << (next-1)))[-next] == "0":
            new_visited = visited | (1 << (next-1))
            new_cost = memo[now][visited]+graph[now-1][next-1]
            if memo[next][new_visited] == 0 or memo[next][new_visited] > new_cost:
                memo[next][new_visited] = new_cost
                q.append((next, new_visited))

min_cost = []
for i in range(2, n+1):
    if graph[i-1][0] != 0 and memo[i][2**n-1] != 0:
        min_cost.append(memo[i][2**n-1]+graph[i-1][0])
print(min(min_cost))
