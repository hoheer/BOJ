import sys


def solution():
    x = int(sys.stdin.readline().rstrip())
    print(str(bin(x)).count('1'))


if __name__ == "__main__":
    solution()
