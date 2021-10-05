from collections import Counter

num = input()

arr = [0 for x in range(0,10)]

for c in num:
    arr[int(c)] += 1

six = arr[6]
arr[6] = 0

nine = arr[9]
arr[9] = 0

mv, mi = max(arr), arr.index(max(arr))
x, y = divmod(six + nine, 2)
sx = x+y

if(mv > sx):
    print(mv)
elif(mv == sx):
    print(mv)
else:
    print(x+y)


