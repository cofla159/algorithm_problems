arr = []
out1 = -1
out2 = -1
flag = False
for _ in range(9):
    arr.append(int(input()))
arr.sort()
for i in range(9):
    if flag == False:
        for j in range(i+1, 10):
            if j == 9 and sum(arr[0:i])+sum(arr[i+1:j]) == 100:
                out1 = i
                out2 = 9
                flag = True
                break
            if sum(arr[0:i])+sum(arr[i+1:j])+sum(arr[j+1:9]) == 100:
                out1 = i
                out2 = j
                flag = True
                break

for i, value in enumerate(arr):
    if i == out1 or i == out2:
        continue
    print(value)
