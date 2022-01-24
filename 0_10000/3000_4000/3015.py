import sys
read = lambda : sys.stdin.readline().strip()


n = int(read())
stack = []
ans = 0
for _ in range(n):
    x = int(read())
    while stack and stack[-1][0] < x:
        ans+= stack.pop()[1]

    if stack and stack[-1][0] == x:
        # 같은게 있으면 cnt를 1씩 늘리는게 이 분기문이 하는 일
        cnt = stack.pop()[1]
        ans+= cnt
        # 2 2 2있으면 젤 앞에 2는 젤 끝에 2를 볼 수 있기 때문에 이렇게 한다.
        if len(stack) != 0 :
            ans += 1
        stack.append((x, cnt+1))
    else:
        if len(stack) != 0 :
            ans += 1
        # 바로 직전의 애와 마주볼 수 있으므로 +1
        stack.append((x, 1))
print(ans)