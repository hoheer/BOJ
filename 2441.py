import sys

a = int(sys.stdin.readline())

i= 0
lst = ['*' for x in range(a)]

print(''.join(lst))
while i < a-1:
    lst[i] = " "
    print(''.join(lst))
    i+=1