import sys

nums = int(sys.stdin.readline().rstrip())
answer = []
while nums > 0:
    nums -= 1
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        answer.pop()
    else:
        answer.append(num)
sum = 0
for n in answer:
    sum += n
print(sum)
