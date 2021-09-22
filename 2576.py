i = 7
num_list = []
while i > 0 :
    num = int(input())
    if(num%2 != 0):
        num_list.append(num)
    i -= 1

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))


