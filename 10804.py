i = 10

nums = [x for x in range(1,21)]
while i>0:
    i-=1

    a,b = map(int,input().split(' '))
    a -= 1

    temp = nums[a:b]
    nums[a:b] = temp[::-1]

for i in nums:
    print(i, end = ' ')