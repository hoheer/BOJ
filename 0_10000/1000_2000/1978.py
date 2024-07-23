import math
import sys


def solution():
    answer = 0
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    for i in range(0, len(num)):
        for j in range(2, num[i]+1):
            if num[i]%j == 0:
                if j == num[i]:
                    answer +=1
                break

    print(answer)


if __name__ == "__main__":
    solution()