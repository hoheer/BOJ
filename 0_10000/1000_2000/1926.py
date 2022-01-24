from sys import stdin
from collections import deque


def solution():
    n, m = map(int, stdin.readline().rstrip().split(' '))
    board = [list(map(int, input().split(' '))) for _ in range(n)]
    check = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    m_size = 0
    p_cnt = 0
    for i in range(0, n):
        for j in range(0, m):
            # new pic
            if board[i][j] == 1 and check[i][j] == 0:
                p_cnt += 1
                # m_size = m_size if m_size >= size else size
                size = 0
                queue.append([i, j])
                check[i][j] = 1
                while len(queue) != 0:
                    # pop current node
                    cur = queue.popleft()
                    x = cur[0]
                    y = cur[1]
                    size += 1

                    # left
                    left = y - 1
                    if left >= 0:
                        if board[x][left] == 1 and check[x][left] == 0:
                            queue.append([x, left])
                            check[x][left] = 1
                    # right
                    right = y + 1
                    if right < m:
                        if board[x][right] == 1 and check[x][right] == 0:
                            queue.append([x, right])
                            check[x][right] = 1

                    # up
                    up = x - 1
                    if up >= 0:
                        if board[up][y] == 1 and check[up][y] == 0:
                            queue.append([up, y])
                            check[up][y] = 1

                    # down
                    down = x + 1
                    if down < n:
                        if board[down][y] == 1 and check[down][y] == 0:
                            queue.append([down, y])
                            check[down][y] = 1
                m_size = m_size if size <= m_size else size
    print(p_cnt)
    print(m_size)


if __name__ == "__main__":
    solution()
