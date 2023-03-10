from sys import stdin


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

    def size(self):
        return self.cnt

    def last_one(self):
        return self.queue[self.i_front]


n = int(stdin.readline())
cards = Queue([i+1 for i in range(n)])

while cards.size() > 1:
    cards.pop()
    cards.push(cards.pop())

print(cards.last_one())
