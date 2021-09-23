def calc(dn: int, edn:int):
    cu = int(edn/dn)
    if(edn%dn != 0 or edn%dn == 0 ):
        cu+=1
    return cu

calls = int(input())
call_len = list(map(int,input().split(' ')))

ys = 0
ms = 0
for i in call_len:
    ys += calc(30,i)*10
    ms +=calc(60,i)*15

if(ys == ms):
    print('Y M',ys)
else:
    print('M',ms) if(min(ms,ys) == ms) else print('Y',ys)