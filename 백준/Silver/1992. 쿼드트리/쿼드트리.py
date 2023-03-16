from sys import stdin

n = int(stdin.readline())
data = []
for _ in range(n):
    data.append(stdin.readline().split()[0])


def quadTree(data, n, x_s, x_e, y_s, y_e):
    if n == 1:
        return data[x_s][y_s]
    lu_ru_ld_rd_index = [(x_s, x_s+n//2-1, y_s, y_s+n//2-1), (x_s+n//2, x_e, y_s,
                                                              y_s+n//2-1), (x_s, x_s+n//2-1, y_s+n//2, y_e), (x_s+n//2, x_e, y_s+n//2, y_e)]
    result = '('
    for index in lu_ru_ld_rd_index:
        zero = False
        one = False
        for i in range(index[2], index[3]+1):
            for j in range(index[0], index[1]+1):
                if data[i][j] == '0':
                    zero = True
                else:
                    one = True
                if zero and one:
                    break
        if zero and not one:
            result += '0'
        elif not zero and one:
            result += '1'
        elif zero and one:
            result += quadTree(data, n//2,
                               index[0], index[1], index[2], index[3])

    result = (result + ')').replace('(0000)', '0').replace('(1111)', '1')
    return result


print(quadTree(data, n, 0, n-1, 0, n-1))
