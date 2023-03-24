from sys import stdin

n, k = map(int, stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(stdin.readline()))

coins.reverse()

answer = 0
for price in coins:
    answer += k//price
    k %= price
print(answer)
