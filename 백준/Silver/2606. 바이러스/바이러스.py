from sys import stdin

c = int(stdin.readline())
cn = int(stdin.readline())
connected = [tuple(map(int, stdin.readline().split())) for _ in range(cn)]
parent = {}
for i in range(1, c+1):
    parent[i] = i


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
        parent[node1_parent] = node2_parent


for edge in connected:
    union_nodes(edge[0], edge[1])

answer = 0
for i in range(1, c+1):
    if i == 1:
        continue
    if get_parent(i) == 1:
        answer += 1

print(answer)
