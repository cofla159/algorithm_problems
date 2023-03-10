from sys import stdin

k = int(stdin.readline())

money = []
for _ in range(k):
    num = int(stdin.readline())
    if num == 0:
        money.pop()
    else:
        money.append(num)

print(sum(money))
