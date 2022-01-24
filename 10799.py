from sys import stdin


def solution():
    bar = stdin.readline().rstrip()
    arr = []
    answer = 0
    lst = '('
    arr2 = []
    for i in bar:
        if i == '(':
            arr.append([i, 0])
            lst = '('
        elif i == ')':
            # laser, last blank was (
            if arr[-1][0] == '(' and lst == '(':
                arr.pop()
                lst = ')'
                arr2.append(len(arr))
            # if end of bar, last blank )
            else:
                arr2.append(1)
                arr.pop()
    print(sum(arr2))


if __name__ == "__main__":
    solution()
