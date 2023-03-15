from sys import stdin
import math

n = int(stdin.readline())
points = []

for _ in range(n):
    points.append(list(map(int, stdin.readline().split())))
points.sort()


def get_distance(point1, point2):
    # 루트 씌우지 않은 값을 반환
    return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2


def divide_by_x(points_list):
    if len(points_list) == 2:    # 그룹이 두개나 세개로 나눠졌으면 그 중 min 값을 리턴
        return get_distance(points_list[0], points_list[1])
    if len(points_list) == 3:
        return min(get_distance(points_list[0], points_list[1]), get_distance(points_list[2], points_list[1]), get_distance(points_list[0], points_list[2]))

    mid = len(points_list) // 2    # 중간에 있는 값을 기준으로 나누기
    if points_list[mid-1] == points_list[mid]:    # 기준값와 바로 옆의 값이 같으면 그대로 리턴
        return 0

    # 왼쪽과 오른쪽의 최솟값 중 작은게 현재까지의 최솟값
    min_distance = min(divide_by_x(
        points_list[:mid]), divide_by_x(points_list[mid:]))

    # 기준값에서 루트(최솟값)만큼 떨어진 영역까지의 점들을 왼쪽과 오른쪽 그룹으로 나눔
    # (왼쪽-왼쪽이나 오른쪽-오른쪽 그룹간은 이미 거리를 구해봤기 때문에 또 진행할 필요가 없음)
    # left_close_points = []
    # right_close_points = []
    # for point in points_list:
    #     if point[0] < points_list[mid][0] and point[0] >= points_list[mid][0] - math.sqrt(min_distance):
    #         left_close_points.append(point)
    #     elif point[0] >= points_list[mid][0] and point[0] <= points_list[mid][0] + math.sqrt(min_distance):
    #         right_close_points.append(point)

    # left_close_points.sort(key=lambda point: point[1])    # y값 기준 정렬
    # right_close_points.sort(key=lambda point: point[1])  # 좌/우 그룹 나눈 것만 다름

    # for point in left_close_points:    # 왼쪽 아래부터 돌면서
    #     # 오른쪽 영역 중 기준점보다 높이가 높은 점들만 거리를 비교
    #     higher = [point for point in right_close_points if point[1]
    #               >= point[1]]
    #     for point2 in higher:
    #         # 최솟값이 나올 수 있는 가장 높은 점은 기준점과 x축으로는 차이가 거의 안나지만 y축으로 최소거리만큼 차이나는 점이므로 이보다 높은 점은 볼 필요가 없음
    #         if point2[1] > point[1] + math.sqrt(min_distance):
    #             break
    #         distance = get_distance(point, point2)
    #         if distance < min_distance:    # 구한 거리가 기존의 최솟값보다 작으면 갱신
    #             min_distance = distance

    close_points = [point for point in points_list if point[0] >= points_list[mid][0] -
                    math.sqrt(min_distance) and point[0] <= points_list[mid][0] + math.sqrt(min_distance)]
    close_points.sort(key=lambda point: point[1])

    for idx, point1 in enumerate(close_points):
        for idx2 in range(idx+1, len(close_points)):
            if close_points[idx2][1] > point1[1] + math.sqrt(min_distance):
                break
            distance = get_distance(point1, close_points[idx2])
            if distance < min_distance:
                min_distance = distance
    return min_distance


print(divide_by_x(points))
