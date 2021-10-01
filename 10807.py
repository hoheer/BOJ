import sys
from collections import Counter

num = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split(' ')))
f_num = int(sys.stdin.readline())
print(Counter(arr)[f_num])


