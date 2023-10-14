from sys import stdin

n, m, r = list(map(int, stdin.readline().split()))
graph = {x+1:[] for x in range(n)}
for _ in range(m):
  a, b = list(map(int, stdin.readline().split()))
  graph[a].append(b)
  graph[b].append(a)

for i in range(n):
  graph[i+1] = sorted(graph[i+1], reverse=True)

visited = [0 for _ in range(n)]
willVisit = [r]
cnt=0

while willVisit:
  now = willVisit.pop()
  if visited[now-1] >0:
    continue
  cnt += 1
  visited[now-1] = cnt
  for next in graph[now]:
    if not visited[next-1]:
      willVisit.append(next)

for ans in visited:
  print(ans)