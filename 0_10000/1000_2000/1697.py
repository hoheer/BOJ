from collections import deque


def ck(n):
    if 0 <= n <= 100000:
        return True
    else:
        return False


answers = []
visit = {}
n, k = map(int, input().split(" "))
loc = deque()
loc.append([n, 0])
sc = 0
while loc:

    tmp = loc.popleft()
    if tmp[0] == k:
        answers.append(tmp[1])
        break

    m1 = tmp[0]-1
    p1 = tmp[0]+1
    d2 = tmp[0]*2

    if ck(m1) and visit.get(m1) == None:
        loc.append([m1, tmp[1]+1])
        visit[m1] = 1
    if ck(p1) and visit.get(p1) == None:
        loc.append([p1, tmp[1]+1])
        visit[p1] = 1
    if ck(d2) and visit.get(d2) == None:
        loc.append([d2, tmp[1]+1])
        visit[d2] = 1

print(answers[0])



