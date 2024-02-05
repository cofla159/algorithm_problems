def solution(p):
    if len(p) == 0:
        return ""
    count = 0
    right_flag = True
    for i in range(len(p)):
        count += 1 if p[i] == "(" else (-1)
        if count < 0:
            right_flag = False
        if count == 0:
            u = p[:i+1] # 앞에서부터 개수가 딱 맞아 떨어질 때 멈추는데 더 분리할 수 있는 경우가 있나?
            v = p[i+1:] if i+1 < len(p) else ""
            break
    if right_flag:
        return u + solution(v)
    else:
        reverse_u = ""
        for c in u[1:-1]:
            if c == "(":
                reverse_u += ")"
            else:
                reverse_u += "("
        result = "(" + solution(v) + ")" + reverse_u
        return result
