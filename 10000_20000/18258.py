import sys
from collections import deque
from sys import stdin


if __name__ == "__main__":
    queue = deque()
    o_num = int(sys.stdin.readline())
    while o_num > 0:
        o_num -= 1
        orders = sys.stdin.readline().rstrip().split(' ')
        if orders[0] == 'push':
            queue.append(orders[1])

        elif orders[0] == 'pop':
            if len(queue) != 0:
                print(queue.popleft())
            else:
                print(-1)

        elif orders[0] == 'size':
            print(len(queue))

        elif orders[0] == 'empty':
            if len(queue) != 0:
                print(0)
            else:
                print(1)

        elif orders[0] == 'front':
            if len(queue) != 0:
                print(queue[0])
            else:
                print(-1)

        elif orders[0] == 'back':
            if len(queue) != 0:
                print(queue[-1])
            else:
                print(-1)

        # print(queue)

