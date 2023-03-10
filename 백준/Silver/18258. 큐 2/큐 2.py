from sys import stdin


class Queue:
    queue = []
    i_front = 0
    i_rear = 0
    cnt = 0

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

    def size(self):
        return self.cnt

    def empty(self):
        return 0 if self.cnt != 0 else 1

    def front(self):
        return self.queue[self.i_front] if self.cnt != 0 else -1

    def back(self):
        return self.queue[self.i_rear-1] if self.cnt != 0 else -1


n = int(stdin.readline())
queue2 = Queue()
for _ in range(n):
    command = stdin.readline().split()
    if command[0] == 'push':
        queue2.push(command[1])
    elif command[0] == 'pop':
        print(queue2.pop())
    elif command[0] == 'size':
        print(queue2.size())
    elif command[0] == 'empty':
        print(queue2.empty())
    elif command[0] == 'front':
        print(queue2.front())
    elif command[0] == 'back':
        print(queue2.back())
