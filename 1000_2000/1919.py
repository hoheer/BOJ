import sys
from collections import Counter

def calc(t1,t2):
    ct1 = Counter(t1)
    ct2 = Counter(t2)
    answer = 0
    std = {}

    for c in set(list(t1)):
        if(ct2[c] != 0):
            std[c] = min(ct1[c],ct2[c])
        else:
            continue
        #공통 문자와 갯수를 구하는 조건을 위에 작성, 하나의 반복문 안에 같이 작성이 가능한가?

    for c in set(list(t1)):
        if(c in std.keys()):
            answer += ct1[c] - std[c]
        else:
            answer += ct1[c]
    for c in set(list(t2)):
        if(c in std.keys()):
            answer += ct2[c] - std[c]
        else:
            answer += ct2[c]

    return answer

tr1 = input()
tr2 = input()

# print((calc(tr1,tr2)calc(tr2,tr1)))
print(calc(tr1,tr2))


# 1. 애너그램의 조건은 같은 문자가 같은 개수만큼 있으면 애너그램의 조건을 만족한다.
# 2. 최장일치문자를 찾아내고(핵심) 이걸 기준으로 하여 카운터 에서 뺴준 갯수의 합을 구하면 된다.
# 3. 최장일치문자열은 어떻게 찾는가? -> 1번 입력을 기준으로 하였을 때, 2번 문자열과 비교를 하는데 먼저 있는 문자 인지 확인을 하는게 1조건, 2조건은 두 카운터 중 작은 개수를 가져와서 설정하면 된다.

