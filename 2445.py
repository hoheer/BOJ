import sys
cnt = int(sys.stdin.readline())

stars = [' ' for x in range(cnt*2)]
save = []
st = 0
ed = len(stars)-1

while ed > st:
    stars[ed] = '*'
    stars[st] = '*'

    ed -=1
    st +=1

    sct = ''.join(stars)
    save.append(sct)
    print(sct)

save.pop()
save = save[::-1]
for c in save:
    print(c)