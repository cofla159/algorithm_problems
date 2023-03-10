from sys import stdin

t = int(stdin.readline())


for _ in range(t):
    ps = []
    line = stdin.readline()
    flag = True
    for char in line:
        if char == '(':
            ps.append('(')
        elif char == ')':
            if len(ps) > 0:
                popped = ps.pop()
                if popped != '(':
                    flag = False
                    break
            else:
                flag = False
                break
    print('NO' if len(ps) > 0 or not flag else 'YES')
