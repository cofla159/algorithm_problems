from sys import stdin

tree = []
while True:
    try:
        tree.append(int(stdin.readline()))
    except:
        break

stack = []
stack.append((0, len(tree)-1))

while stack:
    start, end = stack.pop()
    if start == end:
        print(tree[start])
        continue
    mid = end
    for i in range(start, end+1):
        if tree[i] > tree[start]:
            mid = i-1
            break

    stack.append((start, start))
    if mid+1 <= end:
        stack.append((mid+1, end))
    if start+1 <= mid:
        stack.append((start+1, mid))
