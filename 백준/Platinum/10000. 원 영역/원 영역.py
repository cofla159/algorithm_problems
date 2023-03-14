from sys import stdin
import heapq

n = int(stdin.readline())
circle = []
stop_point = set()    # l이 움직일 지점들, 중복 제거 위해 set
for _ in range(n):
    x, r = list(map(int, stdin.readline().split()))
    # x-r이 같을 경우 x+r이 작은 것부터 정렬하기 위해 x+r 정렬 우선
    heapq.heappush(circle, (x+r, x-r))
    stop_point.add(x-r)    # 원이 시작되고 끊기는 모든 지점을 추가
    stop_point.add(x+r)
# pop으로 작은 것부터 꺼낼 수 있도록 내림차순 정렬
stop_point = sorted(list(stop_point), reverse=True)

sorted_circle = []
while circle:
    popped = heapq.heappop(circle)
    sorted_circle.append([popped[1], popped[0]])    # x-r을 기준으로 정렬할 수 있도록 바꿔 넣고
heapq.heapify(sorted_circle)    # heapify로 정렬

passing = []    # l이 이미 통과중인 원의 끝점을 담을 배열
answer = 1    # 배경은 항상 있는 영역이니까 기본 1
filled = []    # 내부가 채워지는지를 검사해야 하는 배열

while True:
    l = stop_point.pop()    # 가장 작은 지점 꺼내서 시작점으로 지정
    in_circle = []    # 이번 l에서 범위 내로 들어오는 원들을 담을 배열
    flag = False    # filled를 new_filled로 교체해야 하는지
    flag_2 = False    # 첫 번째 while문을 통과하는지
    saved_mid = None

    # sorted_circle에 x-r이 작은 것부터, 같으면 x+r이 작은 것 부터 담겨있기 때문에
    while sorted_circle and sorted_circle[0][0] == l:
        flag_2 = True
        popped = heapq.heappop(sorted_circle)
        in_circle.append(popped)     # in_circle에도,
        heapq.heappush(passing, popped[1])     # pierce에도 x-r(x+r)이 작은 것부터 담김
        answer += 1    # 새로운 원이 추가되므로 일단 카운트 하나 올리기

        # 내부가 채워졌는지 알아볼 리스트(filled)에는 끝점이 작은 것 부터, 끝점이 같다면 시작점이 작은 것부터 담김
        # mid까지 채워진 원을 현재 원(popped)이 이어서 채운다면
        if filled and filled[0][0] == popped[0]:
            if filled[0][1] == popped[1]:    # end에서 끝나야 하는 원인데 현재 원의 끝값이 end와 같으면
                answer += 1                      # 끝까지 채워진 원임
                flag = True    # 아래 else문에서의 new_filled를 filled로 복사하지 않아도 됨
                heapq.heappop(filled)    # 검사 대상에서 제외

            else:
                # 현재 원이 이어서 채우기는 했으나 끝까지 채운건 아니라면 일단 mid를 업데이트하지만 filled를 바꿔버리지는 않고 보류
                # 이거 뒤에 추가되는 원에서 끝까지 채울 수도 있음
                saved_mid = popped[1]
        else:
            flag = True    # filled 리스트가 없는 경우에도 mid를 업데이트 하면 안되므로 flag 바꾸기

    # 현재 l의 위치에서 새로 추가된 원은 있으나(flag_2) 내부가 완전히 채워진 원은 없으면(flag)
    if flag_2 and not flag:
        filled[0][0] = saved_mid     # mid를 아까 저장해둔 것으로 업데이트

    while passing and passing[0] == l:    # l이 완전히 통과한 원이면 passing 배열에서 제거
        popped = heapq.heappop(passing)
        if filled and filled[0][0] == popped:    # 방금 제거한 원의 끝점이 filled의 mid와 같다면
            # filled[0]은 영영 채워지지 않을 경우이므로 제거
            heapq.heappop(filled)

    if len(in_circle) > 1:   # 이번에 추가된 원이 두개 이상이면 무조건 하나가 나머지 하나 안에 들어가므로
        for i, c in enumerate(in_circle):
            if i != 0:    # 가장 작은 원을 빼고
                heapq.heappush(filled,    # filled에는 x+r(=end)이 작은 것부터 담김
                               [in_circle[i-1][1],  c[1]])    # 마지막으로 채워진 지점과 끝까지 채워져야 할 지점을 저장
    if not stop_point:    # 끝까지 다 봤으면 break
        break

print(answer)
