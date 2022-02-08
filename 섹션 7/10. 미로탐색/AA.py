import sys
from collections import deque


def DFS(x, y):
    global cnt

    if x == 6 and y == 6:
        cnt += 1
        return
    else:

        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:  # 남 동 북 서
            if x + i < 0 or y + j < 0 or x + i > 6 or y + j > 6:
                continue
            if res[x + i][y + j] == 0:
                res[x + i][y + j] = 1
                DFS(x + i, y + j)
                res[x + i][y + j] = 0


if __name__ == "__main__":
    res = [list(map(int, input().split())) for _ in range(7)]
    res[0][0] = 1
    cnt = 0

    DFS(0, 0)
    print(cnt)