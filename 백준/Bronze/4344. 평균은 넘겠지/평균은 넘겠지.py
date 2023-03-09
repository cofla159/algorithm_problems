from functools import reduce

c = int(input())
answer = ""
for i in range(c):
    [n, *scores] = list(map(int, input().split(' ')))
    total = reduce(lambda acc, cur: acc+cur, scores, 0)
    average = total/n
    scores.sort(reverse=True)
    for i in range(len(scores)):
        if scores[i] <= average:
            percent = round(i/n*100, 3)
            answer += "{:.3f}".format(percent)+'%\n'
            break
print(answer[:-1])
