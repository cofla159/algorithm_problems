from sys import stdin

n = int(stdin.readline())

k = int(stdin.readline())
apple = []
for _ in range(k):
    apple.append(list(map(int, stdin.readline().split())))

l = int(stdin.readline())
turn = {}
for _ in range(l):
    seconds, dir = stdin.readline().split()
    turn[int(seconds)] = dir


class Queue():
    queue = []
    i_front = 0
    i_rear = 0
    cnt = 0

    def __init__(self, initial_value) -> None:
        self.queue = initial_value
        self.cnt = len(initial_value)
        self.i_rear = self.cnt

    def push(self, x):
        self.queue.append(x)
        self.i_rear += 1
        self.cnt += 1

    def pop(self):
        if self.cnt == 0:
            return -1
        popped = self.queue[self.i_front]
        self.i_front += 1
        self.cnt -= 1
        return popped

    def head(self):
        return self.queue[self.i_rear-1] if self.cnt != 0 else -1

    def contain(self, target):
        if target in self.queue[self.i_front:self.i_rear+1]:
            return True
        return False


snake = {'body': Queue([[1, 1]]), 'direction': 'right'}
time = 0
turn_direction = ['right', 'down', 'left', 'up']

while True:
    time += 1

    direction = snake['direction']
    head_x, head_y = snake['body'].head()
    head = [head_x, head_y+1] if direction == 'right' else [head_x,
                                                            head_y-1] if direction == 'left' else [head_x+1, head_y] if direction == 'down' else [head_x-1, head_y]
    if head[0] > n or head[0] < 1 or head[1] > n or head[1] < 1 or snake['body'].contain(head):
        break

    snake['body'].push(head)
    if head in apple:
        apple.remove(head)
    else:
        snake['body'].pop()

    if turn.get(time):
        now_direction_index = turn_direction.index(snake['direction'])
        if turn[time] == 'L':
            turning_direction_index = now_direction_index - 1
        else:
            turning_direction_index = now_direction_index + \
                1 if now_direction_index != 3 else 0
        snake['direction'] = turn_direction[turning_direction_index]


print(time)
