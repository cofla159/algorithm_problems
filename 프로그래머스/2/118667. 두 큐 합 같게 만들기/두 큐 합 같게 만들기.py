from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1_total = sum(queue1)
    q2_total = sum(queue2)
    total = q1_total+q2_total
    if total % 2 != 0: return -1

    limit = len(queue1) * 4
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    while answer <= limit and q1_total != total // 2:
        if q1_total > q2_total:
            q2.append(q1.popleft())
            q1_total -= q2[-1]
            q2_total += q2[-1]
        else:
            q1.append(q2.popleft())
            q1_total += q1[-1]
            q2_total -= q1[-1]
        answer += 1

    return answer if answer <= limit else -1