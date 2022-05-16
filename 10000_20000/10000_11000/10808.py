import string

answer = {}
for c in string.ascii_lowercase:
    answer[c] = 0

s = input()
for c in s:
    answer[c]+=1

for c in answer:
    print(answer[c], end=' ')

