from sys import stdin

n, c = list(map(int, stdin.readline().split()))
home = []

for i in range(n):
    home.append(int(stdin.readline()))

home.sort()


def install_by_distance(distance, home):
    installed = [home[0]]
    for x in home:
        if x >= installed[-1] + distance:
            installed.append(x)
    return len(installed)


def find_distance(home, number):
    start = 1
    end = home[-1]-home[0]
    answer = -1
    while start <= end:
        mid = (start+end)//2
        installed_num = install_by_distance(mid, home)
        if installed_num >= number:
            if mid > answer:
                answer = mid
                start = mid+1
            else:
                break
        elif installed_num < number:
            end = mid - 1
    return answer


print(find_distance(home, c))
