import sys


def solution():
    a = []
    b = []
    total = [a, b]
    n, m = map(int, sys.stdin.readline().rstrip().split(' '))
    answer = [[0 for j in range(0, m)] for i in range(0, n)]

    for i in range(0, 2):
        for j in range(0, n):
            t = sys.stdin.readline().rstrip().split(' ')
            total[i].append(t)

    for i in range(0, n):
        for j in range(0, m):
            answer[i][j] = int(a[i][j]) + int(b[i][j])

    for i in range(0, n):
        print(*answer[i])


if __name__ == "__main__":
    solution()

