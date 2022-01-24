import sys


# nums == length of array, num == num array
nums = int(sys.stdin.readline().rstrip())
num = []
v = 0
while nums > 0:
    nums -= 1
    num.append(int(sys.stdin.readline().rstrip()))
answer = '+'
arr = [1]
i = 2
for n in num:
    if n not in arr and i > n:
        v = 1
        break
    while i <= n:
        arr.append(i)
        i += 1
        answer += '+'

    arr.pop()
    answer += '-'
if v == 0:
    for o in answer:
        print(o)
elif v == 1:
    print('NO')







