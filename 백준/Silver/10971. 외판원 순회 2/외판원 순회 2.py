n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

node = []
for i in range(1, n):
    node.append(i)

min_cost = 10**7


def get_permutations(arr, selectNumber: int):
    results = []
    global min_cost
    if selectNumber == 1:
        return list(map(lambda x: [x], arr))
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        permutations = get_permutations(rest, selectNumber-1)
        attached = list(map(lambda x: [arr[i], *x], permutations))
        results.extend(attached)
    return results


permutation = get_permutations(node, n-1)

for case in permutation:
    can_i_go = True
    case.append(0)
    sum_cost = 0
    for j in range(n-1):
        if cost[case[j]][case[j+1]] == 0:
            can_i_go = False
            break
        sum_cost += cost[case[j]][case[j+1]]
    
    if cost[case[n-1]][case[0]] == 0:
        can_i_go = False
    if can_i_go == False:
        continue   
    sum_cost += cost[case[n-1]][case[0]]
    if sum_cost < min_cost:
        min_cost = sum_cost

print(min_cost)
