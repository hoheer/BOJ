import sys


class Stack:
    def __init__(self):
        self.array = []

    def push(self, num):
        self.array.append(num)

    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            return self.array.pop()

    def size(self):
        return len(self.array)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.empty() == 1:
            return -1
        else:
            return self.array[self.size()-1]


n = int(sys.stdin.readline().rstrip())
answer = Stack()
while n > 0:
    n -= 1
    orders = list(sys.stdin.readline().rstrip().split(' '))
    order = orders[0]
    if len(orders) > 1:
        num = orders[1]

    if order == 'push':
        answer.push(int(num))
    elif order == 'pop':
        print(answer.pop())
    elif order == 'size':
        print(answer.size())
    elif order == 'empty':
        print(answer.empty())
    elif order == 'top':
        print(answer.top())


