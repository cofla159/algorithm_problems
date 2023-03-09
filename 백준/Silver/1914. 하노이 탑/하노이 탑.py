from sys import stdin

def move(disc: int, start: int, end: int, count: int, output, initialDisc):
    if disc == 1:
        count += 1
        if initialDisc <= 20:
            output.append((start, end))
    else:
        temp = 6 - start - end
        count, output = move(disc-1, start, temp, count, output, initialDisc)
        count, output = move(1, start, end, count, output, initialDisc)
        count, output = move(disc-1, temp, end, count, output, initialDisc)
    return count, output

disc = int(stdin.readline())
count = 0
output = []
if disc <= 20:
    count, output = move(disc, 1, 3, count, output, disc)
else:
    count = 2 ** disc - 1

print(count)
if disc <= 20:
    for a, b in output:
        print(a, b)
