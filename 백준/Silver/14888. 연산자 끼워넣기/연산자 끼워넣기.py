n = int(input())
arr = list(map(int, input().split()))
pl, mi, mul, div = list(map(int, input().split()))

operators = []
for _ in range(pl):
    operators.append('pl')
for _ in range(mi):
    operators.append('mi')
for _ in range(mul):
    operators.append('mul')
for _ in range(div):
    operators.append('div')

memo = {}


def get_combination(arr, selectNumber):
    results = []
    key = tuple(arr)
    if key in memo:
        return memo[key]
    if selectNumber == 1:
        result = list(map(lambda x: [x], arr))
        memo[key] = result
        return result
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        permutations = get_combination(rest, selectNumber-1)
        attached = list(map(lambda x: [arr[i], *x], permutations))
        results.extend(attached)
    memo[key] = results
    return results


combi_operators = list(map(list, list(
    set(map(tuple, get_combination(operators, n-1))))))
min = 10**8
max = -10**8
for combi in combi_operators:
    sum = arr[0]
    for i in range(n-1):
        if combi[i] == 'pl':
            sum += arr[i+1]
        elif combi[i] == 'mi':
            sum -= arr[i+1]
        elif combi[i] == 'mul':
            sum *= arr[i+1]
        else:
            if sum < 0 and arr[i+1] > 0:
                sum = -(-sum//arr[i+1])
            else:
                sum = sum//arr[i+1]
    if sum > max:
        max = sum
    if sum < min:
        min = sum

print(max)
print(min)
