[w, h] = list(map(int, input().split()))
n = int(input())
x = [0]
y = [0]
for i in range(n):
    [dir, size] = list(map(int, input().split()))
    if dir == 0:
        x.append(size)
    else:
        y.append(size)
x.append(h)
y.append(w)
x = sorted(x)
y = sorted(y)
max_x = 0
max_y = 0
for i in range(len(x)-1):
    if x[i+1]-x[i] > max_x:
        max_x = x[i+1] - x[i]
for i in range(len(y)-1):
    if y[i+1]-y[i] > max_y:
        max_y = y[i+1] - y[i]
print(max_x*max_y)
