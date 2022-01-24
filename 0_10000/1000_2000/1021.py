import sys
from collections import deque


def op1(dq):
    return dq.popleft()


def op2(dq):
    dq.append(dq.popleft())


def op3(dq):
    dq.appendleft(dq.pop())


def peek_left(dq):
    return dq[0]


if __name__ == "__main__":
    left = 0
    right = 0
    answer = 0
    qsize, num = map(int, sys.stdin.readline().rstrip().split(' '))
    numbers = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    queue = deque()
    queue_left = deque()
    queue_right = deque()
    for i in range(1, qsize+1):
        queue.append(i)

    queue_right = queue.copy()
    queue_left = queue.copy()
    for n in numbers:
        while peek_left(queue_left) != n:
            op2(queue_left)
            left += 1
        # print("left:", left, queue_left)
        while peek_left(queue_right) != n:
            op3(queue_right)
            right += 1
            # print(queue_right)
        # print("right:", right, queue_right)
        if left <= right:
            queue_left.popleft()
            answer += left
            left = 0
            right = 0
            queue = queue_left.copy()
            queue_right = queue_left.copy()
        elif left > right:
            queue_right.popleft()
            answer += right
            right = 0
            left = 0
            queue = queue_right.copy()
            queue_left = queue_right.copy()
        # print(queue)
    print(answer)