n = input()
inputs = []
for i in range(int(n)):
    inputs.append(input())
for str in inputs:
    score = 0
    correct = 0
    for j in range(len(str)):
        if str[j] == 'O':
            correct += 1
            score += correct
        else:
            correct = 0
    print(score)
