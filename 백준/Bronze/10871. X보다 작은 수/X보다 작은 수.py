[n, x] = list(map(int, input().split(' ')))
numbers = list(map(int, input().split(' ')))

answer = ""
for number in numbers:
    if number < x:
        answer += (str(number) + " ")

print(answer[0:-1])
