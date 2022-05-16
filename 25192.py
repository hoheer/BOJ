import sys
import collections


def solution():
    n = int(sys.stdin.readline().rstrip())
    strs = collections.deque()
    check = collections.deque()
    answer = 0
    tt = 0
    while n > 0:
        n -= 1
        tmp = sys.stdin.readline().rstrip()
        strs.append(tmp)
    for i in range(0, len(strs)):
        if strs[i] == "ENTER":
            answer += len(set(check))
            check = collections.deque()
        elif strs[i] != "ENTER":
            check.append(strs[i])
        if i == len(strs)-1:
            answer += len(set(check))

    print(answer)


if "__name__" == "__main__":
    solution()