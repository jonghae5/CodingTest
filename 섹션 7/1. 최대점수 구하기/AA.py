import sys
# 재귀함수와 스택


def DFS(L, score, t):
    global maxx
    if t > time_res:
        return

    if L == problem_res:
        if score > maxx:
            maxx = score
    else:
        DFS(L + 1, score + res[L][0], t + res[L][1])
        DFS(L + 1, score, t)


if __name__ == "__main__":
    problem_res, time_res = map(int, input().split())

    res = []
    for _ in range(problem_res):
        a, b = map(int, input().split())
        res.append([a, b])

    # res[0] 점수 res[1] 시간
    maxx = -2147000000
    DFS(0, 0, 0)
    print(maxx)