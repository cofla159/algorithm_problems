def solution(s):
    if len(s) == 1:
        return 1
    answer = 1000
    for i in range(1, len(s)//2 + 1): # i글자 단위로 자름
        temp = ""
        index, count = 0, 1
        while index < len(s):
            if s[index:index+i] == s[index+i:index+2*i]:
                count += 1
            else:
                temp += str(count) + s[index:index+i] if count > 1 else s[index:index+i]
                count = 1
            index += i
        answer = min(answer, len(temp))
            
    return answer
