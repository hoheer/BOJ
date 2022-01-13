import sys
from sys import stdin
from collections import deque


def shake(q):
    while len(q) != 1:
        q.popleft()
        q.append(q.popleft())
    return q


if __name__ == "__main__":
    num = int(sys.stdin.readline().rstrip())
    queue = deque()

    for n in range(1,num+1):
        queue.append(n)
    after_shake = shake(queue)
    print(after_shake[0])
