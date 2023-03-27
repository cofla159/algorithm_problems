from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

lis = [None]*n
lis[0] = (1, nums[0])
answer = 1
for i in range(1, n):
    flag = False
    max_lis = -1
    for j in range(i):
        if lis[j][1] < nums[i] and lis[j][0] > max_lis:
            max_lis = lis[j][0]
            flag = True
    if flag:
        lis[i] = (max_lis+1, nums[i])
        answer = max(answer, max_lis+1)
    if not flag:
        min_last = nums[i]
        for k in range(j):
            if lis[k][1] < min_last:
                min_last = lis[k][1]
        lis[i] = (1, min_last)

print(answer)
