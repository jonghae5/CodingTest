
import sys
from collections import deque

if __name__ =="__main__":
    n,m = map(int,input().split())
    MAX = 100000
    queue = deque()
    dis=[0] * (MAX+1)
    # 체크 여부
    ch=[0]* (MAX+1)
    ch[n] = 1
    queue.append(n)
    cnt=0
    method = [-1,1,5]

    while queue:

        problem = queue.popleft()
        if problem <0:
            continue
        cnt = dis[problem] + 1

        for i in range(3):
            problem +=method[i]
            if ch[problem] ==0:
                ch[problem] = 1
                dis[problem] = cnt
                queue.append(problem)
                if problem == m:
                    print(cnt)
                    sys.exit(0)
            problem -=method[i]

