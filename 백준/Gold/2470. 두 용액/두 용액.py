from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()


def find_sol2(sol1_index, sol1, arr):
    start = sol1_index+1
    end = len(arr)-1
    answer = (10**9-1, sol1)
    while start <= end:
        mid = (start+end)//2
        result = arr[mid] + sol1
        if result == 0:
            answer = (result, arr[mid])
        else:
            if abs(answer[0]) > abs(result):
                answer = (result, arr[mid])
            if result < 0:
                start = mid+1
            else:
                end = mid-1
    return answer


if arr[0] > 0:
    print(f'{arr[0]} {arr[1]}')
elif arr[-1] < 0:
    print(f'{arr[-2]} {arr[-1]}')
else:
    left = 0
    right = len(arr)-1
    answer = ((10**9-1, 0, 0))
    while left < right:
        result = arr[left]+arr[right]
        if result == 0:
            answer = (result, arr[left], arr[right])
            break
        else:
            if abs(result) < abs(answer[0]):
                answer = (result, arr[left], arr[right])
            if result < 0:
                left += 1
            else:
                right -= 1
    print(f'{answer[1]} {answer[2]}')