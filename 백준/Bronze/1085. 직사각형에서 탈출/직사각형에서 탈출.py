[x, y, w, h] = list(map(int, input().split(' ')))

min_width = x if w-x > x else w-x
min_heigh = y if h-y > y else h-y
print(min_width if min_width < min_heigh else min_heigh)
