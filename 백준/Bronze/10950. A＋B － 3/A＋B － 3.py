test_num = int(input())
answer = ""
for i in range(test_num):
    numbers = list(map(int, input().split(' ')))
    answer += str(numbers[0]+numbers[1])+'\n'
print(answer)
