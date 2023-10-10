from sys import stdin

n = int(stdin.readline().strip())
a = list(map(int, stdin.readline().split()))
b,c = list(map(int, stdin.readline().split()))

answer = 0
for i in range(n):
  rest = a[i]-b
  answer += 1
  if rest > 0:
    answer += rest // c +1 if rest % c != 0 else rest // c

print(answer)