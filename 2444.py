import sys

cnt = int(sys.stdin.readline())
blank = [' ' for x in range(cnt)]
save = []
stars = '*'
for i in range(cnt):
    blank.pop()
    sct = ''.join(blank) + stars
    save.append(sct)
    print(sct)
    stars += '**'

save.pop()
save = save[::-1]
for s in save:
    print(s)