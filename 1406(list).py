import sys

stc: str = sys.stdin.readline().rstrip()
order_cnt = int(input())
answer = stc

while order_cnt > 0:
    order_cnt -= 1
    order = list(sys.stdin.readline().rstrip().split(' '))


    if order[0] == 'L':
        if cursor == 0:
            continue
        cursor -= 1

    elif order[0] == 'D':
        if cursor == lst.cnt:
            continue
        cursor += 1

    elif order[0] == 'B':
        if cursor == 0:
            continue
        else:
            lst.remove(cursor)
            cursor -= 1

    elif order[0] == 'P':
        lst.insert(order[1], cursor)
        cursor += 1


