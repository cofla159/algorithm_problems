def solution(n, arr1, arr2):
    arr = [[' ' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        str1 = change_num_to_2num(arr1[i], n)
        str2 = change_num_to_2num(arr2[i], n)
        for j in range(n):
            if str1[j] == '1' or str2[j] == '1':
                arr[i][j] = '#'
    return [''.join(line) for line in arr]

def change_num_to_2num(num, max_len):
    answer = ''
    for i in range(max_len-1, -1, -1):
        if num - 2**i >= 0:
            answer += '1'
            num -= 2**i
        else:
            answer += '0'
    return answer
        
        
# 이진수로 변환
# 11111 일때 2^4+2^3+2^2+2^1+2^0
# n % 2^5