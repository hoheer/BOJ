import sys


answer = [0]
top_cnt = int(sys.stdin.readline().rstrip())
towers = list(map(int, sys.stdin.readline().rstrip().split(' ')))
arr = [0]
for i in range(1, top_cnt):
    # stack init
    while len(arr) > 0:
        if towers[arr[-1]] > towers[i]:
            answer.append(arr[-1]+1)
            arr.append(i)
            break
        arr.pop()
        if len(arr) == 0:
            arr.append(i)
            answer.append(0)
            break


    # # push to stack
    # if towers[i] < towers[arr[-1]]:
    #     arr.append(i)
    #     answer.append(arr[-1])


for a in answer:
    print(a, end = ' ')



