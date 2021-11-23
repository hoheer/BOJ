import sys

stars = int(sys.stdin.readline())
blank = [' ' for x in range(stars+1)]
blank.pop()
star = '*'
for i in range(stars):
    blank.pop()
    print(''.join(blank) + star)
    star += '**'
