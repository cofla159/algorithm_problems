from sys import stdin

n, k = list(map(int, stdin.readline().split()))
levels = []

for _ in range(n):
    levels.append(int(stdin.readline()))

levels.sort()

T = sorted(levels)[0]


def get_k(desired, levels):
    sum = 0
    for x in levels:
        if x < desired:
            sum += desired - x
    return sum


start = levels[0]
end = levels[-1] + k
max_T = levels[0]
while start <= end:
    mid = (start+end)//2
    needed_k_tobe_mid = get_k(mid, levels)
    if needed_k_tobe_mid == k:
        max_T = mid
        break
    elif needed_k_tobe_mid < k:
        if mid > max_T:
            max_T = mid
        start = mid + 1
    else:
        end = mid - 1

print(max_T)
