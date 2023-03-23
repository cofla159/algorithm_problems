from sys import stdin
import heapq

n, k = map(int, stdin.readline().split())
test_tube = []
pq = []
for i in range(n):
    row = list(map(int, stdin.readline().split()))
    for j in range(n):
        if row[j] > 0:
            heapq.heappush(pq, [row[j], i, j])
    test_tube.append(row)
s, target_x, target_y = map(int, stdin.readline().split())
target_x -= 1
target_y -= 1

time = 0
for _ in range(s):
    tmp_stack = []

    while pq:
        now_num, now_x, now_y = heapq.heappop(pq)
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_x, new_y = now_x+x, now_y+y
            if 0 <= new_x < n and 0 <= new_y < n and test_tube[new_x][new_y] == 0:
                test_tube[new_x][new_y] = now_num
                tmp_stack.append([now_num, new_x, new_y])

    for kan in tmp_stack:
        heapq.heappush(pq, kan)

print(test_tube[target_x][target_y])
