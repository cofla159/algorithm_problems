def solution(s):
    answer = ""
    eng_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    while s:
        if s[0].isnumeric():
            answer += str(s[0])
            s = s[1:]
        else:
            for i, eng in enumerate(eng_num):
                if s.startswith(eng):
                    answer += str(i)
                    s = s[len(eng):]
                    break
    return int(answer)