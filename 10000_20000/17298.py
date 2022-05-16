import sys


n = int(sys.stdin.readline().rstrip())
narr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
aarr = [0]
answer = [-1] * n
for i in range(1, n):
    while len(aarr) > 0:
        if narr[aarr[-1]] < narr[i]:
            answer[aarr[-1]] = narr[i]
            aarr.pop()
        else:
            break
    aarr.append(i)
for n in answer:
    print(n, end = ' ')
