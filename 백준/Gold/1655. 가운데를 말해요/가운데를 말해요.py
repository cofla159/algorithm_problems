from sys import stdin
import heapq

n = int(stdin.readline())
min_heapq = []
max_heapq = []
median = 10**5+1

for _ in range(n):
    num = int(stdin.readline())
    if (len(min_heapq) == 0 and len(max_heapq) == 0) or num <= median:
        heapq.heappush(max_heapq, -num)
    elif num > median:
        heapq.heappush(min_heapq, num)

    if len(min_heapq) > len(max_heapq):
        heapq.heappush(max_heapq, -heapq.heappop(min_heapq))
    elif len(min_heapq)+1 < len(max_heapq):
        heapq.heappush(min_heapq, -heapq.heappop(max_heapq))

    median = -max_heapq[0]
    print(median)
