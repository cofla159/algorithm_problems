from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    combi = [defaultdict(int) for _ in range(max(course)+1)]
    
    # 14*18 = 252
    # 20 * 10 * 252 = 50400
    for order in orders:
        for num in course:
            for c in combinations(order, num):
                combi[num]["".join(sorted(c))] += 1
                
    for dic in combi:
        if len(dic) > 0:
            max_ordered = max(dic.values())
            answer.extend([k for k,v in dic.items() if v == max_ordered and v  > 1])             
    return sorted(answer)