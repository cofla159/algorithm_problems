n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
total = [i for i in range(1,n)]
answer = 1980
dp = {str(x):0 for x in range(n)}

def getScore(people):
  score = 0
  # 0,1 계산하고 0,1,2 계산하면 이전값 활용해야되는데 못함
  for i in range(len(people)-1):
    for j in range(i+1, len(people)):
      a = people[i]
      b = people[j]
      score += s[a][b] + s[b][a]
  return score

def pickOne(teamA, rest):
  global answer
  if len(teamA) == n/2:
    aPeople = ",".join(map(str, sorted(teamA)))
    bPeople = ",".join(map(str, sorted(rest)))
    if bPeople not in dp:
      bScore = getScore(rest)
      dp[bPeople] = bScore
    else:
      bScore = dp[bPeople]
    diff = abs(dp[aPeople]-bScore)
    answer = min(answer, diff)
    return
  for i in range(len(rest)):
    plusedKeyA = ",".join(map(str, sorted(teamA+[rest[i]])))
    if plusedKeyA not in dp:
      # 현재까지의 teamA 점수계산
      score = 0
      for p in teamA:
        score += s[p][rest[i]] + s[rest[i]][p]
      originKeyA = ",".join(map(str, sorted(teamA)))
      dp[plusedKeyA] = dp[originKeyA]+score if originKeyA != "" else score
      pickOne(teamA+[rest[i]], rest[0:i]+rest[i+1:])



pickOne([0], total)
print(answer)