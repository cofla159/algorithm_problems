from sys import stdin

n = int(stdin.readline().rstrip())
a = stdin.readline().rstrip()
graph = [[] for _ in range(n)]
for i in range(n-1):
    u, v = stdin.readline().split()
    u = int(u)-1
    v = int(v)-1
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
indoor_num = a.count('1')
if indoor_num <= 1:
    print(0)
elif indoor_num == 2:
    print(2)
else:
    for x in range(n):
        if a[x] == '0':
            continue
        stack = [x]
        visited = [False]*n
        visited[x] = True
        while stack:
            now = stack.pop()
            for i in graph[now]:
                if not visited[i] and a[i] == '1':
                    cnt += 1
                elif not visited[i]:
                    stack.append(i)
                    visited[i] = True

print(cnt)
