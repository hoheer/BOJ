import sys


def solution():
    nums = [0 for i in range(30)]
    for i in range(0, 28):
        q = int(sys.stdin.readline().rstrip())
        nums[q-1] = q

    for i in range(0, 30):
        if nums[i] == 0:
            print(i+1)

if __name__ == "__main__":
    solution()



