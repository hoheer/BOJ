import sys

arr_len = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))
x = int(input())

# 이 문제는 이중포문으로 풀리긴하는데 엔^2 로는 시간제한에 걸릴 것으로 생각된다.
# dict 를 사용하면 2n 시간 내에 풀이가 가능하다.
dict = {}
answer = 0
for i in range(arr_len):
        dict[arr[i]] = i
    #한번 순회로 n 추가
# print(dict)
for i in arr:
    try:
        if(dict[x-i] != -1):
            answer += 1
        if((x-i) ==i):
            answer -= 1
    except:
        continue
print(int(answer/2))