from sys import stdin
import heapq


k, n = list(map(int, stdin.readline().split()))
primes = list(map(int, stdin.readline().split()))
numbers = [1]  # 곱할 대상 숫자
total_numbers = []  # n번째 숫자를 찾을 배열
overlapped = set()  # 중복 검사
answer = 2**31
cnt = 0

while True:
    num = heapq.heappop(numbers)
    if num >= answer:
        break
    for sub in primes:
        new_num = num*sub
        if new_num > answer:
            continue
        if new_num in overlapped:
            continue
        cnt += 1
        heapq.heappush(numbers, new_num)
        overlapped.add(new_num)
        heapq.heappush(total_numbers, -new_num)
        if cnt == n:
            answer = -heapq.heappop(total_numbers)
            break
        if cnt > n:
            answer = min(answer, -heapq.heappop(total_numbers))

print(answer)
