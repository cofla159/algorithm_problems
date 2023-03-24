import sys
sys.setrecursionlimit(1000000)

n = int(input())
memo = {1: 1, 2: 2}

for i in range(3, n+1):
    memo[i] = (memo[i-1]+memo[i-2]) % 15746


print(memo[n])
