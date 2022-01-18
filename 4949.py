from sys import stdin

bk = ['[', '(']
out = [']', ')']
while True:
    s = input().rstrip()
    if s == '.':
        break
    arr = []
    sign = 1
    for c in s:
        if c in bk:
            arr.append(c)
        if c == ']':
            if arr and arr[-1] == '[':
                arr.pop()
            else:
                sign = 0
                break
        elif c == ')':
            if arr and arr[-1] == '(':
                arr.pop()
            else:
                sign = 0
                break
    if not arr and sign:
        print("yes")
    else:
        print("no")




    # print(s)
