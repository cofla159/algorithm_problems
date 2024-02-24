from collections import deque

def solution(board):
    n = len(board)
    queue = deque()
    dp = [[[0] * 4 for _ in range(n)] for _ in range(n)]
    x_dir = [0,-1,0,1]
    y_dir = [-1,0,1,0]
    
    queue.append([2,[0,0]])
    queue.append([3,[0,0]])
    count = 0
    
    while queue:
        prev_i, now = queue.popleft()

        for i in range(4):
            nxt = [now[0]+x_dir[i],now[1]+y_dir[i]]
            if nxt[0] < 0 or nxt[0] > n-1 or nxt[1] < 0 or nxt[1] > n-1 or nxt == [0,0] or board[nxt[0]][nxt[1]] == 1:
                continue

            price = dp[now[0]][now[1]][i] + 100 if prev_i == i else dp[now[0]][now[1]][prev_i] + 600

            if dp[nxt[0]][nxt[1]][i] == 0 or dp[nxt[0]][nxt[1]][i] > price:
                queue.append([i, nxt])
                dp[nxt[0]][nxt[1]][i] = price
            
    return min([x for x in dp[n-1][n-1] if x != 0])

# bfs
# 방향에 상관없이 갈 수 있는 길이면 스택에 추가.
# 여기서 갈 수 있는 길이라는 것은 안 가봤거나 가봤는데 가격이 지금 이 더 싸거나
# 방문 체크는 따로 할 필요 X. dp에 뭔가 들어있으면 그게 방문체크.
# 단순히 가격이 낮을때만 dp에 갱신하면 안됨. 현재까지는 더 쌌는데 다음 칸으로 가는 순간 방향전환이 생기면서 더 비싸지는 경우가 있을 수 있기 때문.

# bfs 말고 dfs
# 위와 같은 이유로 방문했던 곳의 이전 가격이 더 싸더라도 재방문해야 하는데 그럼 bfs로는 끝나지 않음
# dfs로 각각의 경우에 대해 독립적으로 값을 구해야 함
# dp도 필요없고 스택의 원소에 같이 가격을 가지고 있기
# 그렇다고 방문체크를 전혀 안하면 영원히 안끝남
# 한 경우(한 라인) 안에서는 재방문을 막아야 함

# bfs로도 되는데, 역전되는 상황을 위해 방향별로 메모이제이션을 따로 하도록
# dp=[x][y][방향]으로 저장해야 함