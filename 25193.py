import sys

n = int(sys.stdin.readline().rstrip())
foods = sys.stdin.readline().rstrip()
c = 0
o = 0

c_c = 0
c_o = 0

for i in foods:
    if i == 'C':
        c += 1
    else:
        o += 1


