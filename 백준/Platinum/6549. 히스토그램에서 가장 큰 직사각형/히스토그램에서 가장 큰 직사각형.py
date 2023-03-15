from sys import stdin


def get_max_area(start, end, histogram):
    if end-start == 0:
        return histogram[start]
    elif end-start == 1:
        return max(2*min(histogram[start], histogram[end]), max(histogram[start], histogram[end]))

    mid = (start+end) // 2
    max_area = max(get_max_area(start, mid, histogram),
                   get_max_area(mid+1, end, histogram))

    if histogram[mid] < histogram[mid+1]:
        max_height = histogram[mid+1]
        s = mid+1
        e = mid+1
    else:
        max_height = histogram[mid]
        s = mid
        e = mid

    extended_area = max_height
    while True:
        if s-1 < start and e+1 > end:
            break
        if (s-1 < start and e+1 <= end) or (e+1 <= end and histogram[s-1] < histogram[e+1]):
            e += 1
            max_height = min(max_height, histogram[e])
        else:
            s -= 1
            max_height = min(max_height, histogram[s])
        extended_area = max_height*(e-s+1)
        if extended_area > max_area:
            max_area = extended_area

    return max_area


while True:
    input_str = stdin.readline().split()
    if input_str[0] == '0':
        break

    n, *histogram = list(map(int, input_str))
    print(get_max_area(0, n-1, histogram))
