import sys
cnt = int(sys.stdin.readline())

sarr = ['*' for x in range(cnt*2+1)]
blank = []
save = []

for i in range(cnt):
    sarr.pop()
    sarr.pop()
    sct = ''.join(blank) + ''.join(sarr)
    save.append(sct)
    print(sct)

    blank.append(' ')

save.pop()
save = save[::-1]
for c in save:
    print(c)


