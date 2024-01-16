from collections import defaultdict

def solution(N, stages):
    answer = []
    ongoing = [0] * (N+2)
    for stage in stages:
            ongoing[stage] += 1
            
    failure = []
    total = 0
    for i in range(N+1, 0, -1):
        total += ongoing[i]
        if i <= N and total == 0:
            failure.append((i, 0))
        elif i <= N:
            failure.append((i, ongoing[i] / total))
    
    failure.sort()
    failure.sort(key=lambda x:x[1], reverse=True)
    return [x[0] for x in failure]