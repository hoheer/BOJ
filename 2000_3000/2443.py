import sys

cnt = int(sys.stdin.readline())

star = ['*' for x in range(cnt*2-1)]
blank = []

for i in range(cnt):
    print(''.join(blank) + ''.join(star))
    blank.append(' ')
    if(i != cnt-1):
        star.pop()
        star.pop()

