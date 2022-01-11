import sys
from sys import stdin


class Queue:
    def __init__(self):
        self.arr = []

    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if self.empty() != 1:
            print(self.arr.pop(0))
        else:
            print(-1)

    def size(self):
        print(len(self.arr))

    def empty(self):
        result = 1 if len(self.arr) == 0 else 0
        return result

    def front(self):
        if self.empty() != 1:
            print(self.arr[0])
        else:
            print(-1)

    def back(self):
        if self.empty() != 1:
            print(self.arr[-1])
        else:
            print(-1)


if __name__ == "__main__":
    queue = Queue()
    o_num = int(sys.stdin.readline())
    while o_num > 0:
        o_num -= 1
        orders = sys.stdin.readline().rstrip().split(' ')
        if orders[0] == 'push':
            queue.push(orders[1])
        elif orders[0] == 'pop':
            queue.pop()
        elif orders[0] == 'size':
            queue.size()
        elif orders[0] == 'empty':
            print(queue.empty())
        elif orders[0] == 'front':
            queue.front()
        elif orders[0] == 'back':
            queue.back()

        # print(queue.arr)

