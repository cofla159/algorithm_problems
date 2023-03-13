from sys import stdin

m, n, l = list(map(int, stdin.readline().split()))
guns = (list(map(int, stdin.readline().split())))
animals = []
for _ in range(n):
    animals.append(list(map(int, stdin.readline().split())))

guns.sort()
answer = 0


def hit_at_shooting_range(l, gun, animal, x_max, x_min):
    if animal[0] > x_max or animal[0] < x_min or animal[1] > l:
        return -1
    if l >= gun-animal[0]+animal[1] and l >= -gun + animal[0] + animal[1]:
        return True
    if l >= gun-animal[0]+animal[1]:
        return '+'
    if l >= -gun + animal[0] + animal[1]:
        return '-'


x_max = guns[-1]+l
x_min = guns[0]-l

for animal in animals:
    start = 0
    end = len(guns)-1

    while start <= end:
        mid = (start+end)//2
        result = hit_at_shooting_range(l, guns[mid], animal, x_max, x_min)
        if result == True:
            answer += 1
            break
        elif result == -1:
            break
        elif result == "+":
            start = mid+1
        elif result == '-':
            end = mid - 1

print(answer)
