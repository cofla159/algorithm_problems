from sys import stdin

n, k = map(int, stdin.readline().split())
electric = list(map(int, stdin.readline().split()))
multitab = [0]*n
cnt = 0
next_empty = 0
for i in range(k):
    if electric[i] in multitab:
        continue
    elif next_empty < n:
        multitab[next_empty] = electric[i]
        next_empty += 1
    else:
        early = set()
        for j in range(i+1, k):
            if electric[j] in multitab:
                early.add(electric[j])
            if len(early) == n-1:
                break
        last_one = list(set(multitab)-early)
        if len(last_one) > 0:
            multitab[multitab.index(last_one[0])] = electric[i]
        else:
            multitab[0] = electric[i]
        cnt += 1
print(cnt)
