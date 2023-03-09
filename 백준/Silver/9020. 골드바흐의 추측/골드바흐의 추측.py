n = int(input())


def decimal(number: int):
    if number == 1:
        return False
    elif number == 2 or number == 3:
        return True
    for i in range(2, number-1):
        if number % i == 0:
            return False
    return True


for _ in range(n):
    t = int(input())
    if t == 4:
        print('2 2')
        continue
    for i in range(t//2):
        # print(t, i, t//2+i, t//2-i)
        if (t//2+i) % 2 != 0:
            if decimal(t//2+i) == True and decimal(t//2-i) == True:
                print(f'{t//2-i} {t//2+i}')
                break
