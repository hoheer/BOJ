import sys
from collections import deque
import re


if __name__ == "__main__":
    cnt_case = int(sys.stdin.readline().rstrip())
    while cnt_case > 0:
        queue = deque()
        cnt_case -= 1

        # order
        order = sys.stdin.readline().rstrip()
        # order = order.replace("RR", '')

        # len
        arr_len = int(sys.stdin.readline().rstrip())

        # arr
        arr = sys.stdin.readline()
        arr = re.sub('[^0-9]', ' ', arr).strip().split(' ')
        # queue = deque(map(int, [c for c in arr if c]))
        queue = deque([c for c in arr if c])

        result = 0
        r = 0
        for o in order:
            if o == 'R':
                r += 1
            elif o == 'D':
                if len(queue) != 0 and r%2 == 0:
                    queue.popleft()

                elif len(queue) != 0 and r%2 != 0:
                    queue.pop()

                else:
                    result = "error"
                    break
        if result == "error":
            print("error")
        else:
            if r % 2 == 0:
                print("[" + ','.join(queue) + "]")

            elif r % 2 != 0:
                queue.reverse()
                print("[" + ','.join(queue) + "]")






