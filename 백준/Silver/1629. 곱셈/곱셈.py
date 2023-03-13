from sys import stdin

a, b, c = list(map(int, stdin.readline().split()))

numbers = {}


def involution(a, b, c):
    if b == 0:
        numbers[0] = 1
        return 1
    result = numbers.get(b//2)
    if result:
        return result*result % c if b % 2 == 0 else result*result*a % c
    else:
        result = involution(a, b//2, c)
        numbers[b//2] = result
        return result*result % c if b % 2 == 0 else result*result*a % c


print(involution(a, b, c))
