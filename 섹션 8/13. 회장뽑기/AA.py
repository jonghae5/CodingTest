import sys
from collections import deque
import itertools as it

if __name__ == "__main__":
    n = int(input())
    board = [[100] * n for _ in range(n)]
    ch = [0] * (n+1)

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        board[a-1][b-1] = 1
        board[b-1][a-1] = 1

    for k in range(n):
        for l in range(n):
            for m in range(n):
                if l ==m:
                    continue
                board[l][m] = min(board[l][m],board[l][k] + board[k][m])

    result =[]

    for i in range(n):
        val = 0
        for j in range(n):
            if board[i][j] == 100 :
                continue
            if board[i][j] > val:
                val = board[i][j]
        result.append(val)

    cnt = 0
    people = []
    for i in range(len(result)):
        if result[i] == min(result):
            cnt+=1
            people.append(i+1)

    print(min(result), cnt)
    for people in people:
        print(people,end=' ')


