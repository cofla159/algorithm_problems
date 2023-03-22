from sys import stdin
from collections import deque

n, k = stdin.readline().split()
n = int(n)
k = int(k)
coins = set()
for _ in range(n):
    coins.add(int(stdin.readline()))
coins = list(coins)
stack = deque([[[], 0]])
already_in_sum = [False]*(k+1)
answer = -1
while stack:
    now_comb, now_sum = stack.popleft()
    if now_sum == k:
        answer = len(now_comb)
        break
    for i, price in enumerate(coins):
        new_comb = now_comb+[price]
        new_sum = now_sum + price
        if new_sum <= k and not already_in_sum[new_sum]:
            stack.append([new_comb, new_sum])
            already_in_sum[new_sum] = True

print(answer)
