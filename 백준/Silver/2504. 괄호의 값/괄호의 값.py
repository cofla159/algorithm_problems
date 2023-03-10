from sys import stdin

pr = list(stdin.readline())
score = 0
flag = []
temp_score = []
for i in range(len(pr)):
    if pr[i] == '(' or pr[i] == '[':
        if (pr[i] == '(' and pr[i+1] == ')') or (pr[i] == '[' and pr[i+1] == ']'):
            if len(flag) == 0:
                score += 2 if pr[i] == '(' else 3
            else:
                temp_score[-1] += 2 if pr[i] == '(' else 3
            pr[i+1] = ' '
        else:
            flag.append('(' if pr[i] == '(' else '[')
            temp_score.append(0)
    elif pr[i] == ')' or pr[i] == ']':
        if len(flag) == 0 or (pr[i] == ']' and flag[-1] != '[') or (pr[i] == ')' and flag[-1] != '('):
            score = 0
            break
        else:
            popped = temp_score.pop()
            temp = popped * 2 if pr[i] == ')' else popped * 3
            flag.pop()
            if len(flag) == 0:
                score += temp
            else:
                temp_score[-1] += temp

print(score)
