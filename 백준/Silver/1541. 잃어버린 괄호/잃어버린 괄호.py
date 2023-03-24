str = input() + '+'

flag = False
answer = 0
num = ''
for char in str:
    if char == '+' or char == '-':
        if flag:
            answer -= int(num)
        else:
            answer += int(num)
        num = ''
        if char == '-':
            flag = True
    else:
        num += char
print(answer)
