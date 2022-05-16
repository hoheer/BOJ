import sys
from collections import Counter

ip = 'Impossible'
ps = 'Possible'

cases = int(sys.stdin.readline())
for cs in range(cases):
    a, b = input().split(' ')
    rs = ps
    if(len(a) != len(b)):
        rs = ip
    else:
        ca = Counter(a)
        cb = Counter(b)
        for c in b:
            if(ca[c]!=cb[c]):
                rs = ip
                break
    print(rs)




