a = int(input())
b = int(input())
c = int(input())
mul = str(a*b*c)
answer = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
          '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for i in range(len(mul)):
    answer[mul[i]] += 1
for i in answer:
    print(answer[i])
