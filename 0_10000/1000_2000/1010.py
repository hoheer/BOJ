import sys


def solution():
    t = int(sys.stdin.readline().rstrip())
    answer = []

    # test case
    for i in range(t):
        a, b = map(int, sys.stdin.readline().rstrip().split(" "))

        # b에서 a만큼 뽑는 가짓수 구하면 됨 (조합)
        tmp = b
        tmp2 = a
        m_tmp = 1
        s_tmp = 1
        for j in range(a):
            m_tmp = m_tmp * tmp
            tmp -= 1
            s_tmp = s_tmp * tmp2
            tmp2 -= 1

        answer.append(int(m_tmp/s_tmp))

    for k in answer:
        print(k)

if __name__ == "__main__":
    solution()





