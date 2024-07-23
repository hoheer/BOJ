import sys


def solution():
    while 1:
        a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))
        nums = [a, b, c]
        mn = max(nums)
        nums.remove(mn)

        if mn == 0:
            break
        if (mn*mn) == ((nums[0]*nums[0]) + (nums[1]*nums[1])):
            print("right")
        else:
            print("wrong")


if __name__ == "__main__":
    solution()
