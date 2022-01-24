from sys import stdin
from collections import deque


def solution():
    n, m = map(int, stdin.readline().split(' '))
    maze = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    queue = deque()

    # maze start
    queue.append([0, 0])
    dist[0][0] = 0
    # bfs start
    while queue:
        cur = queue.popleft()
        x = cur[0]
        y = cur[1]
        dis = dist[x][y]

        # left
        left = y - 1
        if left >= 0:
            if maze[x][left] == 1 and dist[x][left] < 0:
                queue.append([x, left])
                dist[x][left] = dis+1
        # right
        right = y + 1
        if right < m:
            if maze[x][right] == 1 and dist[x][right] < 0:
                queue.append([x, right])
                dist[x][right] = dis+1
        # up
        up = x - 1
        if up >= 0:
            if maze[up][y] == 1 and dist[up][y] < 0:
                queue.append([up, y])
                dist[up][y] = dis+1
        # down
        down = x + 1
        if down < n:
            if maze[down][y] == 1 and dist[down][y] < 0:
                queue.append([down, y])
                dist[down][y] = dis + 1

    print(dist[n-1][m-1]+1)





    return 1


if __name__ == "__main__":
    solution()
