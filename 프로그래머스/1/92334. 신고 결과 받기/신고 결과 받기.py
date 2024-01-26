from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = defaultdict(int) # 신고당한 횟수
    mail = defaultdict(list) # 자기가 신고한 사람
    blocked = set() # 정지된 사람
    
    for r in report:
        sender, receiver = r.split(" ")
        if receiver not in mail[sender]:
            reported[receiver] += 1
            mail[sender].append(receiver)
        if reported[receiver] >= k:
            blocked.add(receiver)
    
    for i, user in enumerate(id_list):
        for report in mail[user]:
            if report in blocked:
                answer[i] += 1
            
    return answer