from sys import stdin

n = int(stdin.readline())
tree = []

for _ in range(n):
    tree.append(stdin.readline().split())


def print_front(root, result):
    result += tree[root][0]
    if tree[root][1] != '.':
        for i, node in enumerate(tree):
            if node[0] == tree[root][1]:
                result = print_front(i, result)
                break
    if tree[root][2] != '.':
        for i, node in enumerate(tree):
            if node[0] == tree[root][2]:
                result = print_front(i, result)
                break
    return result


def print_middle(root, result):
    if tree[root][1] != '.':
        for i, node in enumerate(tree):
            if node[0] == tree[root][1]:
                result = print_middle(i, result)
                break
    result += tree[root][0]
    if tree[root][2] != '.':
        for i, node in enumerate(tree):
            if node[0] == tree[root][2]:
                result = print_middle(i, result)
                break
    return result


def print_back(root, result):
    if tree[root][1] != '.':
        for i, node in enumerate(tree):
            if node[0] == tree[root][1]:
                result = print_back(i, result)
                break
    if tree[root][2] != '.':
        for i, node in enumerate(tree):
            if node[0] == tree[root][2]:
                result = print_back(i, result)
                break
    result += tree[root][0]
    return result


print(print_front(0, ''))
print(print_middle(0, ''))
print(print_back(0, ''))
