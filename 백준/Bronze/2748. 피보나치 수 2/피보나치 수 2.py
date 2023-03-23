import sys
sys.setrecursionlimit(100000)
n = int(input())

memo = {0: 0, 1: 1}


def fibo(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if not memo.get(x-1):
        memo[x-1] = fibo(x-1)
    if not memo.get(x-2):
        memo[x-2] = fibo(x-2)

    return memo[x-1]+memo[x-2]


print(fibo(n))
