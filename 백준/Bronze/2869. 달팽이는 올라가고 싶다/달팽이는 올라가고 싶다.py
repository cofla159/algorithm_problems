import math

[a, b, v] = list(map(int, input().split()))
days = math.ceil((v-a)/(a-b))
print(days+1)
