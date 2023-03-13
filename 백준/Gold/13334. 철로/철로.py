from sys import stdin
import heapq

n = int(stdin.readline())
commute = []
cut_point = set()

for _ in range(n):
    way = list(map(int, stdin.readline().split()))
    if way[0] < way[1]:
        way = [way[1], way[0]]
    cut_point.add(way[0])
    heapq.heappush(commute, way)

d = int(stdin.readline())

cut_point = list(cut_point)
cut_point.sort(reverse=True)
# commute = [x for x in commute if x[0]-x[1] <= d]

l_end = cut_point.pop()
l_start = l_end-d

contained_heapq = []
answer = 0
while True:
    while len(commute) > 0 and commute[0][0] <= l_end:
        heapq.heappush(contained_heapq, heapq.heappop(commute)[1])
    while len(contained_heapq) > 0 and contained_heapq[0] < l_start:
        heapq.heappop(contained_heapq)
    contained_num = len(contained_heapq)
    if contained_num > answer:
        answer = contained_num
    if len(commute) == 0:
        break
    l_end = cut_point.pop()
    l_start = l_end-d

print(answer)
