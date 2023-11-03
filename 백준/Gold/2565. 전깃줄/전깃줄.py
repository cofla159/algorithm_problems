from sys import stdin
  
    
n = int(stdin.readline())
lines = []
for _ in range(n):
  lines.append(list(map(int, stdin.readline().split())))
lines.sort()
dp=[1] * n
# i번째까지 최대로 교차하지 않고 연결될 수 있는 수

for i in range(1,n):
  for j in range(i):
    if lines[j][1] < lines[i][1]: dp[i] = max(dp[i], dp[j]+1)
  
print(n-max(dp))