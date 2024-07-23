import sys


def solution():
    nums = []
    for i in range(0, 3):
        tnum = sys.stdin.readline().rstrip()
        nums.append(tnum)

    print((int(nums[0]) + int(nums[1])) - int(nums[2]))
    print(int(nums[0]+nums[1]) - int(nums[2]))


if __name__ == "__main__":
    solution()