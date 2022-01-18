from sys import stdin


if __name__ == "__main__":
    bk = ['(']
    cnt = int(stdin.readline().rstrip())
    while cnt > 0:
        arr = []
        cnt -= 1
        stc = stdin.readline().rstrip()
        flag = 1
        for c in stc:
            if c == '(':
                arr.append(c)
            elif c == ')':
                if arr and arr[-1] == '(':
                    arr.pop()
                else:
                    flag = 0
                    break
        if not arr and flag:
            print("YES")
        else:
            print("NO")

