import sys


def solution():
    stc = sys.stdin.readline().rstrip()

    if stc == "A+":
        print("4.3")
    elif stc == "A0":
        print("4.0")
    elif stc == "A-":
        print("3.7")
    elif stc == "B+":
        print("3.3")
    elif stc == "B0":
        print("3.0")
    elif stc == "B-":
        print("2.7")
    elif stc == "C+":
        print("2.3")
    elif stc == "C0":
        print("2.0")
    elif stc == "C-":
        print("1.7")
    elif stc == "D+":
        print("1.3")
    elif stc == "D0":
        print("1.0")
    elif stc == "D-":
        print("0.7")
    else:
        print("0.0")


if __name__ == "__main__":
    solution()
