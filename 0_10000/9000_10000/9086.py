import sys


def solution():
    case = int(sys.stdin.readline().rstrip())

    for i in range(0, case):
        stc = sys.stdin.readline().rstrip()
        print(stc[0]+stc[-1])


if __name__ == "__main__":
    solution()