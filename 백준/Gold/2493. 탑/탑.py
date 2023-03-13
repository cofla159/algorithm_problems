from sys import stdin

n = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
towers.reverse()

stack = [0]
answer = [0]*n

for i in range(1, n):
    while len(stack) > 0 and towers[i] > towers[stack[-1]]:
        last = stack.pop()
        answer[last] = n-i
    stack.append(i)


print(*reversed(answer))
