import sys
a, b = map(int,sys.stdin.readline().split(' '))
rooms = {}
answer = 0

for p in range(a):
    sex, grade = sys.stdin.readline().rstrip().split(' ')
    key = sex+grade

    if key in rooms.keys():
        if rooms[key] < b:
            rooms[key] += 1
        else:
            answer+=1
            rooms[key] = 1
    else:
        rooms[key] = 1
        answer+=1

print(answer)
