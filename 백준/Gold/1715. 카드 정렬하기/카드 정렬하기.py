from sys import stdin
import heapq

n = int(stdin.readline())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(stdin.readline()))

cards_sum = 0
for i in range(n-1):
    sum_of_two = heapq.heappop(cards)+heapq.heappop(cards)
    cards_sum += sum_of_two
    heapq.heappush(cards, sum_of_two)


print(cards_sum if n > 1 else 0)
