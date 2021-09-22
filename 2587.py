nums: int = []
for i in range(0,9):
    nums.append(int(input()))

sums = sum(nums)
cha = sums - 100

i = 0
j = 8

nums.sort()
while j>i:
    temp = nums[i] + nums[j]
    if(temp > cha):
        j -= 1
    elif(temp < cha):
        i += 1
    else:
        break

a= nums[i]
b= nums[j]


nums.remove(a)
nums.remove(b)

for i in nums:
    print(i, end = ' ')

