from sys import stdin

n = int(stdin.readline())
schedule = []
for _ in range(n):
  schedule.append(list(map(int, stdin.readline().split(" "))))
dp=[0]*(n+1)

# 처음~오늘까지 훑으면서 일 안하고 오늘 vs 그날에 일해서 오늘 돈 받을 수 있는 경우의 max값 구하기
# 오늘까지 일한걸 오늘 당장 받을수 있다고 하면 그날 일했는지 안했는지 체크 안하고 또 일하는 경우가 생기게 됨
# (예제 4에서 1일차에 일해서 5일에 50을 받으면 5일차에 또 일하는걸로 되어서 60이 생김)
# => k일동안 일한 돈은 k+1일에 받는다고 생각하자
# ==> n일동안 일한 돈을 구하려면 n+1일차까지 구해야 함

for i in range(n+1): # i=0~n
  for j in range(i): # j=0~i-1
    dp[i] = max(dp[i], dp[j]) # 최소값 갱신
    if j+schedule[j][0] == i:
      dp[i] = max(dp[i], dp[j]+schedule[j][1])

print(dp[-1])
