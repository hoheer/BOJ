import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    tsize = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    t, p = map(int, sys.stdin.readline().rstrip().split(' '))

    sorder = 0
    porder = 0

    for i in range(0, len(tsize)):
        if tsize[i]%t > 0:
            sorder += int(tsize[i]/t) + 1
        else:
            sorder += int(tsize[i]/t)

    porder += int(n/p) + n%p

    print(str(sorder))
    print(str(int(n/p)) + " " + str(n%p))


if __name__ == "__main__":
    solution()