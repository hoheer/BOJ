import sys

def solution() :
    n = int(sys.stdin.readline().rstrip())
    c, b = map(int, sys.stdin.readline().rstrip().split(" "))
    order = c/2 + b
    answer = order if max(n, order) == n else n;
    print(int(answer))

