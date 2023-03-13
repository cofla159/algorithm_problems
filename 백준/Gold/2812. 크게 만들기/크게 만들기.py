from sys import stdin

n, k = list(map(int, stdin.readline().split()))
num = list(map(int, stdin.readline().split()[0]))
# first_num = max(num[:n-k+1])
answer1 = num.copy()
removed_times = 0

# for char in num:
#     if char < first_num:
#         answer1.remove(char)
#         removed_times += 1
#     else:
#         break


answer2 = []
while removed_times < k:
    answer2 = [answer1[0]]
    flag = False
    for i in range(1, len(answer1)):
        while len(answer2) > 0 and answer2[-1] < answer1[i] and removed_times < k:
            answer2.pop()
            flag = True
            removed_times += 1
        answer2.append(answer1[i])
        if removed_times == k:
            answer2.extend(answer1[i+1:])
            break
    if flag == False:
        answer2 = answer2[:n-k]
        break
    answer1 = answer2

print(''.join(map(str, answer2)))
