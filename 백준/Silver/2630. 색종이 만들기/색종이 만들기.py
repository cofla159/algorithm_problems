from sys import stdin

n = int(stdin.readline())
paper = []
for _ in range(n):
    paper.append(stdin.readline().split())
white = 0
blue = 0


def cut(start_x, end_x, start_y, end_y, arr):
    global white, blue
    flag_cut = False
    for index_y in range(start_y, end_y+1):
        if '1' in arr[index_y][start_x:end_x+1] and "0" in arr[index_y][start_x:end_x+1]:
            flag_cut = True
            break
        elif '1' in arr[index_y][start_x:end_x+1]:
            flag_cut = 'blue' if flag_cut == False or flag_cut == 'blue' else True
        elif '0' in arr[index_y][start_x:end_x+1]:
            flag_cut = 'white' if flag_cut == False or flag_cut == 'white' else True
        else:
            flag_cut = True
    if flag_cut == True:
        cut(start_x, (start_x+end_x)//2, start_y, (start_y+end_y)//2, arr)
        cut((start_x+end_x)//2+1, end_x, start_y, (start_y+end_y)//2, arr)
        cut(start_x, (start_x+end_x)//2, (start_y+end_y)//2+1, end_y, arr)
        cut((start_x+end_x)//2+1, end_x, (start_y+end_y)//2+1, end_y, arr)
    elif flag_cut == 'blue':
        blue += 1
    else:
        white += 1


cut(0, n-1, 0, n-1, paper)
print(white, blue)
