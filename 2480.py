from collections import Counter

nums = []
nums = list(map(int,input().split()))

cnt = len(Counter(nums).keys())

if(cnt == 1):
    print(10000+nums[0]*1000)
elif(cnt == 2):
    print(Counter(nums).most_common(1)[0][0]*100 + 1000)
else:
    print(max(nums)*100)