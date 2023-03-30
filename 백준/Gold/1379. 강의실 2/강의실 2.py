from sys import stdin
import heapq

n = int(stdin.readline())
lecture = []
for _ in range(n):
    lecture.append(list(map(int, stdin.readline().split())))

# lecture.sort(key=lambda x: x[2])
lecture.sort(key=lambda x: x[1])

classroom = []
heapq.heappush(classroom, [lecture[0][2],  1])  # 끝나는 시간, 강의 번호, 강의실 번호
answer = [None]*(n+1)  # k번호 강의의 강의실 번호
answer[lecture[0][0]] = 1

for i in range(1, n):
    if classroom[0][0] > lecture[i][1]:
        heapq.heappush(classroom, [lecture[i][2], len(classroom)+1])
        answer[lecture[i][0]] = len(classroom)
    else:
        _, room_num = heapq.heappop(classroom)
        heapq.heappush(classroom, [lecture[i][2], room_num])
        answer[lecture[i][0]] = room_num

print(len(classroom))
for i in range(1, n+1):
    print(answer[i])
