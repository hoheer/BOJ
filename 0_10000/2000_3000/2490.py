import string

apb = string.ascii_uppercase
dict = {}

dict = {num+1: apb[num] for num in range(0,4)}
i = 3
while i >0:
    i -= 1
    yut = list(map(int,input().split(' ')))
    answer = (yut.count(0))
    if answer == 0:
        print('E')
    else:
        print(dict[yut.count(0)])