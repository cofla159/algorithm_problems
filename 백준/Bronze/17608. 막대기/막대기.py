from sys import stdin

n = int(stdin.readline())
sticks = []
answer = 0

for _ in range(n):
    sticks.append(int(stdin.readline()))

sticks.reverse()
highest = 0
for stick in sticks:
    if stick > highest:
        answer += 1
        highest = stick

print(answer)
