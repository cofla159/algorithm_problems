from sys import stdin

stack = []


def push(x):
    stack.append(x)


def pop():
    print(stack.pop() if len(stack) > 0 else -1)


def size():
    print(len(stack))


def empty():
    print(0 if len(stack) > 0 else 1)


def top():
    print(stack[-1] if len(stack) > 0 else -1)


n = int(stdin.readline())
for _ in range(n):
    command = stdin.readline().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'top':
        top()
