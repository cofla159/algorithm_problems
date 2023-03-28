from sys import stdin

n = int(stdin.readline())
meetings = []
for _ in range(n):
    meetings.append(list(map(int, stdin.readline().split())))

meetings.sort()
meetings.sort(key=lambda x: x[1])

cnt = 0
endtime = 0
for i in range(n):
    if meetings[i][0] >= endtime:
        cnt += 1
        endtime = meetings[i][1]

print(cnt)
