# 재귀함수와 스택
import sys
sys.stdin = open("input.txt","r")


'''강의 풀이'''


# def DFS1():
#     cnt=3
#     print(cnt)
# # def DFS2():
# #     if cnt ==5:
# #         cnt = cnt+1 # 지역변수 선언 > 이러면 에러가 난다. 전역변수를 찾으러가지 않기 때문이다.
# #         print(cnt)
# def DFS2():
#     global cnt
#     if cnt ==5:
#         cnt = cnt+1 # 전역변수를 가져와 전역변수를 수정한다.
#         print(cnt)
# if __name__ =="__main__":
#     cnt = 5
#     DFS1()
#     DFS2()
#     print(cnt)

def DFS1():
    a[0] = 7 # 새로운 변수를 선언하는 것이 아닌 인덱스 안에 있는 값을 변경한다. (참조 역할)
    print(a)

def DFS2():
    global a
    a = a+[7] # 지역변수 선언 > 이러면 에러가 난다. 전역변수를 찾으러가지 않기 때문이다.
    print(a)
def DFS():
    a = [4,5,6]
    print(a)

if __name__ == "__main__":
    a = [1,2,3]
    DFS1()
    DFS()
    print(a)
    DFS2()