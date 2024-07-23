import sys


def solution():
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))

    print((a+b)*(a-b))


if __name__ == "__main__":
    solution()