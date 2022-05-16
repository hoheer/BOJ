import sys
from sys import stdin
from collections import deque


def solution(orders, dq):
    if orders[0] == "push_front":
        dq.appendleft(orders[1])

    elif orders[0] == "push_back":
        dq.append(orders[1])

    elif orders[0] == "pop_front":
        if len(dq) != 0:
            print(dq.popleft())
        else:
            print(-1)

    elif orders[0] == "pop_back":
        if len(dq) != 0:
            print(dq.pop())
        else:
            print(-1)

    elif orders[0] == "size":
        print(len(dq))

    elif orders[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif orders[0] == "front":
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)

    elif orders[0] == "back":
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)


if __name__ == "__main__":
    order_num = int(sys.stdin.readline().rstrip())
    queue = deque()
    while order_num > 0:
        # cnt
        order_num -= 1
        # insert order
        orders = sys.stdin.readline().rstrip().split(' ')
        solution(orders, queue)