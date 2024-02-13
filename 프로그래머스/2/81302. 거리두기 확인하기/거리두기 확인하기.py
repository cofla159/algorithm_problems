def solution(places):
    answer = []
    for place in places:
        result = 1
        for i in range(5):
            if not result:
                break
            for j in range(5):
                if place[i][j] == "P":
                    if (i>0 and place[i-1][j] == "P") or (j>0 and place[i][j-1] == "P") or (i < 4 and place[i+1][j] == "P") or (j < 4 and place[i][j+1] == "P"):
                        result = 0
                        break
                    elif (i > 1 and place[i-2][j] == "P" and place[i-1][j] != "X") or (j >1 and place[i][j-2] == "P" and place[i][j-1] != "X") or (i < 3 and place[i+2][j] == "P" and place[i+1][j] != "X") or (j < 3 and place[i][j+2] == "P" and place[i][j+1] != "X"):
                        result = 0
                        break
                    elif (i>0 and j>0 and place[i-1][j-1] == "P" and (place[i-1][j] != "X" or place[i][j-1] != "X")) or (i<4 and j>0 and place[i+1][j-1] == "P" and (place[i][j-1] != "X" or place[i+1][j] != "X")) or (i>0 and j<4 and place[i-1][j+1] == "P" and (place[i-1][j] != "X" or place[i][j+1] != "X")) or (i<4 and j<4 and place[i+1][j+1] == "P" and (place[i+1][j] != "X" or place[i][j+1] != "X")):
                        result = 0
                        break
        answer.append(result)
    return answer