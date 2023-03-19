from sys import stdin

v, e = list(map(int, stdin.readline().split()))
graph = []
for _ in range(e):
    graph.append(list(map(int, stdin.readline().split())))

parent = {}
for i in range(v):
    parent[i+1] = i+1


def get_parent(child):
    if parent[child] == child:
        return child
    parent[child] = get_parent(parent[child])
    return parent[child]


def union_nodes(node1, node2):
    node1_parent = get_parent(node1)
    node2_parent = get_parent(node2)
    if node1_parent > node2_parent:
        parent[node1_parent] = node2_parent
    else:
        parent[node2_parent] = node1_parent


graph.sort(key=lambda x: x[2])

cost = 0
connected = 0
for road in graph:
    if connected == v-1:
        break
    if get_parent(road[0]) == get_parent(road[1]):
        continue
    cost += road[2]
    connected += 1
    union_nodes(road[0], road[1])

print(cost)
