from sys import stdin
import sys
sys.setrecursionlimit(10**7)

str1 = stdin.readline().rstrip()
str2 = stdin.readline().rstrip()
len_1 = len(str1)
len_2 = len(str2)

memo = [[0]*(len_1+1) for _ in range(len_2+1)]

for i in range(1, len_2+1):
    for j in range(1, len_1+1):
        if str1[j-1] == str2[i-1]:
            memo[i][j] = memo[i-1][j-1]+1
        else:
            memo[i][j] = max(memo[i][j-1], memo[i-1][j])

print(memo[len_2][len_1])
