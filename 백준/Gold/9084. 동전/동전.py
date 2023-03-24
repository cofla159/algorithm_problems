# 9084 동전
import sys
input = sys.stdin.readline


def dp(m, i):
    """0번째 동전부터 i번째 동전까지 사용해 m을 만들 수 있는 경우의 수"""
    if m < 0:
        return 0
    if value_case[i][m] is not None:
        return value_case[i][m]
    if i == 0:  # 사용할 수 있는 동전이 끝의 동전 하나일 때
        if m % coins[i] == 0:  # 하나의 동전으로 나누어 떨어지면
            value_case[i][m] = 1
        else:
            value_case[i][m] = 0
    else:
        now_coin = coins[i]
        value_case[i][m] = dp(m, i-1) + dp(m-now_coin, i)  # i번째 동전을 쓰거나 안 쓰거나
    return value_case[i][m]


T = int(input())
for _ in range(T):
    N = int(input())
    coins = tuple(map(int, input().split()))
    M = int(input())
    value_case = [[None]*(M+1) for _ in range(N)]

    print(dp(M, N-1))
