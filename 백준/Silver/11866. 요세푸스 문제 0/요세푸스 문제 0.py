n, k = list(map(int, input().split()))
answer = []
people = [i for i in range(1, n+1)]
start_idx = 0
cnt = n
while len(people) > 0:
    new_idx = (start_idx+k-1) % cnt
    answer.append(people.pop(new_idx))
    cnt -= 1
    start_idx = new_idx
print('<'+', '.join(map(str, answer))+'>')
