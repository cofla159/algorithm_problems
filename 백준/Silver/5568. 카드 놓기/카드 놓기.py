n = int(input())
k = int(input())
cards = []
for _ in range(n):
    cards.append((input()))


def getPermutations(arr, select_number):
    results = []
    if select_number == 1:
        return arr
    for i, fixed in enumerate(arr):
        combinations = getPermutations([*arr[:i], *arr[i+1:]], select_number-1)
        attached = map(lambda x: x+fixed, combinations)
        results.extend(attached)
    return results


print(len(set(getPermutations(cards, k))))
