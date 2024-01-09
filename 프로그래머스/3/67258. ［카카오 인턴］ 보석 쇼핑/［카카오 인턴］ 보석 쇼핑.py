from collections import defaultdict


def solution(gems):
    answer = []
    low, high = 0, 0
    kind = len(set(gems))
    cart = defaultdict(int)
    cart[gems[0]] = 1

    while high < len(gems) and low < len(gems):
        if len(cart) == kind:
            answer.append([low + 1, high + 1])
            cart[gems[low]] -= 1
            if cart[gems[low]] == 0:
                del cart[gems[low]]
            low += 1
        else:
            high += 1
            if high < len(gems):
                cart[gems[high]] += 1

    answer.sort()
    answer.sort(key=lambda x: x[1] - x[0])
    return answer[0]
