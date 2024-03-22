def solution(tickets):
    tickets.sort(key = lambda x : (x[0], x[1]))
    answer = ["ICN"]
    visited = [0] * len(tickets)
    # print("sorted tickes:", tickets)
    
    answer, _, _ = recursive(answer, visited, tickets)
    return answer

def recursive(answer, visited, tickets):
    # print("call recursive with answer, visited, tickets: ",answer, visited, tickets)
    if len(answer) == len(tickets) + 1:
        return answer, visited, tickets
    for i, ticket in enumerate(tickets+tickets):
        if ticket[0] == answer[-1] and not visited[i % len(tickets)]:
            visited[i % len(tickets)] = 1
            answer.append(ticket[1])
            # print("answer에 추가", visited, answer)
            answer, visited, tickets = recursive(answer, visited, tickets)
            # print("returned answer, visited, tickets:", answer, visited, tickets)
            if len(answer) == len(tickets) + 1:
                return answer, visited, tickets
            else:
                visited[i % len(tickets)] = 0
                answer.pop()
                # print("넣었던거 취소", visited, answer)
    return answer, visited, tickets