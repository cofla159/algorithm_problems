def solution(board, moves):
    basket = []
    n = len(board)
    new_board = []
    picked = 0
    
    for i in range(n):
        temp = []
        for j in range(n):
            if board[j][i] != 0:
                temp.append(board[j][i])
        new_board.append(temp)
        
    for move in moves:
        if len(new_board[move-1]):
            picked += 1
            got = new_board[move-1].pop(0)
            if len(basket) and basket[-1] == got:
                basket.pop()
            else:
                basket.append(got)

    return picked-len(basket)