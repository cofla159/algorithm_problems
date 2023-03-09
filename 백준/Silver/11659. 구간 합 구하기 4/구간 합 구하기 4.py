from sys import stdin
from functools import reduce

n, m = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))
accumulate_sum = [arr[0]]
for i in range(1, n):
    accumulate_sum.append(accumulate_sum[i-1]+arr[i])
    
accumulate_sum.insert(0, 0)
for _ in range(m):
    i, j = list(map(int, stdin.readline().split()))
    print(accumulate_sum[j]-accumulate_sum[i-1])
