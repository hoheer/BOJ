import sys


bud_cnt = int(sys.stdin.readline().rstrip())
building = []
answer = 0
for i in range(bud_cnt):
    building.append(int(sys.stdin.readline().rstrip()))
arr = [building[0]]
for i in range(1, bud_cnt):
    while len(arr) > 0:
        if arr[-1] <= building[i]:
            arr.pop()
        else:
            break
    arr.append(building[i])
    # print(len(arr))
    if len(arr) > 1:
        answer += len(arr)-1
print(answer)


