from sys import stdin

n, m = list(map(int, stdin.readline().split()))

graph = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
parent = {}
for i in range(n):
    parent[i+1] = i+1


def get_parent(child):
    if parent[child] == child:
        return child
    parent[child] = get_parent(parent[child])
    return parent[child]


def union_nodes(node1, node2):
    node1_parent = get_parent(node1)
    node2_parent = get_parent(node2)
    if node1_parent < node2_parent:
        parent[node2_parent] = node1_parent
    else:
        parent[node2_parent] = node1_parent


for edge in graph:
    union_nodes(edge[0], edge[1])

total_parents = set()

for node in range(1, n+1):
    total_parents.add(get_parent(node))

print(len(total_parents))
