n = int(input())
A = list(map(int, input().split()))
pl,mi,mul,di = list(map(int, input().split()))
operators = []
for _ in range(pl):
  operators.append("+")
for _ in range(mi):
  operators.append("-")
for _ in range(mul):
  operators.append("*")   
for _ in range(di):
  operators.append("/")

maxValue = -10**10
minValue = 10**10
dp={}

def reflection(used, operators, value):
  global maxValue, minValue
#   print("refle called",used,operators,value)
  if len(operators) == 0:
    # print(value,maxValue, minValue)
    maxValue = max(maxValue, value)
    minValue = min(minValue, value)
    # print(value,maxValue, minValue)
    return
  for i,op in enumerate(operators):
    if op == "+" and not used+"+" in dp:
      newValue = value + A[n-len(operators)]
      dp[used+"+"] = newValue
      del operators[i]
      reflection(used+"+", operators, newValue)
      operators.insert(i, "+")
    elif op == "-" and not used+"-" in dp:
      newValue = value - A[n-len(operators)]
      dp[used+"-"] = newValue
      del operators[i]
      reflection(used+"-", operators, newValue)
      operators.insert(i, "-")
    elif op == "*" and not used+"*" in dp:
      newValue = value * A[n-len(operators)]
    #   print("new:",newValue)
      dp[used+"*"] = newValue
      del operators[i]
      reflection(used+"*", operators, newValue)
      operators.insert(i, "*")
    elif op == "/" and not used+"/" in dp:
      if value < 0:
        newValue = -(-value // A[n-len(operators)])
      else:
        newValue = value // A[n-len(operators)]
      dp[used+"/"] = newValue
      del operators[i]
      reflection(used+"/", operators, newValue)
      operators.insert(i, "/")

reflection("", operators, A[0])
print(maxValue)
print(minValue)