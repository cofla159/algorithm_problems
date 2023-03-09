import math

n = int(input())
a = list(map(int, (input().split())))
a.sort()
if n % 2 == 0:
    b = [None] * n
    for i in range(int(n/2)):
        index_larger = n/2-1 + (i+1 if i % 2 != 0 else i) * (-1)**(i+1)
        b[int(index_larger)] = a[n-i-1]
        index_smaller = n/2 + (i+1 if i % 2 != 0 else i) * (-1)**i
        b[int(index_smaller)] = a[i]
else:
    b = [None]*(n+1)
    for i in range(int((n-1)/2)):
        index_larger = n/2 + (i+1 if i % 2 != 0 else i) * (-1)**(i+1)
        b[int(index_larger)] = a[n-i-1]
        index_smaller = n/2 + 1 + (i+1 if i % 2 != 0 else i) * (-1)**i
        b[int(index_smaller)] = a[i]
    if abs(a[int((n-1)/2)] - b[1]) > abs(a[int((n-1)/2)] - b[n-1]):
        b[0] = a[int((n-1)/2)]
    else:
        b[n] = a[int((n-1)/2)]
b = list(filter(lambda x: x != None, b))
sum = 0
for i in range(len(b)-1):
    sum += abs(b[i]-b[i+1])
print(sum)
