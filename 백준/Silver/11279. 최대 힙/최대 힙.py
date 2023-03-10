import heapq
from sys import stdin

arr = []
n = int(stdin.readline())
for _ in range(n):
    x = int(stdin.readline())
    if x > 0:
        heapq.heappush(arr, -x)
    else:
        if len(arr) > 0:
            print(-heapq.heappop(arr))
        else:
            print(0)
