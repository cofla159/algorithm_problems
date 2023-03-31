n, r, c = list(map(int, input().split()))

number = 0


def Z(x: int, y: int, m: int, target: list[int]):
    # print(f'called Z({x},{y}, {m}, {target})')
    global number
    if m <= 2:
        if x == target[0] and y+1 == target[1]:
            number += 1
        elif x+1 == target[0] and y == target[1]:
            number += 2
        elif x+1 == target[0] and y+1 == target[1]:
            number += 3
        print(number)
        return
    half = m//2
    divide = [x+half, y+half]
    # print(target[0], divide[0], target[1], divide[1])
    if target[0] < divide[0] and target[1] >= divide[1]:  # 2
        number += (m**2)//4
        # print(f'number: {number}')
        Z(x, y+half, half, target)
    elif target[0] >= divide[0] and target[1] < divide[1]:  # 3
        number += (m**2)//4*2
        # print(f'number: {number}')
        Z(x+half, y, half, target)
    elif target[0] >= divide[0] and target[1] >= divide[1]:  # 4
        number += (m**2)//4*3
        # print(f'number: {number}')
        Z(x+half, y+half, half, target)
    else:  # 1
        Z(x, y, half, target)


Z(0, 0, 2**n, [r, c])
