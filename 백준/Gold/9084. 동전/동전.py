from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    cases = [0]*(m+1)
    cases[0] = 1
    for price in coins:
        for i in range(1, m+1):
            if i-price >= 0:
                cases[i] += cases[i-price]

    print(cases[m])
