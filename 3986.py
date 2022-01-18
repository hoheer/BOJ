from sys import stdin


w_cnt = int(stdin.readline().rstrip())
answer = 0
while w_cnt > 0:
    w_cnt -= 1
    arr = []
    words = stdin.readline().rstrip()
    for c in words:
        if c == 'A':
            if arr and arr[-1] == 'A':
                arr.pop()
            else:
                arr.append(c)
        elif c == 'B':
            if arr and arr[-1] == 'B':
                arr.pop()
            else:
                arr.append(c)
    if len(arr) == 0:
        answer += 1
print(answer)


