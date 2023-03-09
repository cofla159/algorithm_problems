from sys import stdin

n = int(stdin.readline())
a = sorted(list(map(int, stdin.readline().split())))

m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))


def binary_search(target, arr, n):
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return True
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid-1
    return False


for num_b in b:
    print(1 if binary_search(num_b, a, n) else 0)
