import sys
import heapq as hq

'''강의 풀이'''
# 최대힙은 입력할 때 부호를 바꾸어 버린다.
a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n ==0 :
        if len(a) ==0 :
            print(-1)
        else:
            print(-hq.heappop(a)) # 출력을 양수로
    else:
        hq.heappush(a,-n) # 부호를 바꾸어 놓음

