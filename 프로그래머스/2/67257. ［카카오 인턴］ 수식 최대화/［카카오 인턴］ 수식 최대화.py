from itertools import permutations

def solution(expression):
    operators = set()
    split = []
    temp = ""
    
    for i, c in enumerate(expression):
        if c.isdecimal():
            temp += c
            if i == len(expression)-1:
                split.append(temp)
        else:
            split.append(temp)
            temp = ""
            split.append(c)
            operators.add(c)
    
    answer = 0
    for priority in permutations(operators, len(operators)):
        temp = split[:]
        result = []
        for pri in priority:
            i = 0
            while len(temp) > 1 and i < len(temp):
                if temp[i] == pri:
                    operand1 = result.pop()
                    operand2 = temp[i+1]
                    result.append(str(eval(operand1+pri+operand2)))
                    i += 2
                else:
                    result.append(temp[i])
                    i += 1
            temp = result[:]
            result = []
        answer = max(abs(int(temp[0])), answer) 
        
    return answer