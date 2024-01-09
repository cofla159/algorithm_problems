from collections import defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for line in edge:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
                
    node_by_cost = defaultdict(list)
    willVisit = [(1, 0)]
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    
    while(willVisit):
        now, cost = willVisit.pop(0)
        node_by_cost[cost].append(now)
        for next in graph[now]:
            if not visited[next]:
                willVisit.append((next, cost+1))
                visited[next] = 1
    
    max_cost = max(node_by_cost.keys())
    return len(node_by_cost[max_cost])