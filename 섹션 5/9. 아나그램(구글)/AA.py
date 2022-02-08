from collections import deque
'''오종해 풀이'''

def dict_func():
    word = input()
    res = dict()
    for word in word:
        if word in res.keys():
            res[word] += 1
        else:
            res[word] = 1
    return res

res1 = dict_func()
res2 = dict_func()

for key, val in res1.items():
    if (key not in res2.keys()) or (val != res2[key]):
        print("NO")
        break
else:
    print("YES")


# '''리스트 해쉬 아스키 코드 : 65 ~ 90 대문자 , 97 ~ 122 소문자'''
# a = input()
# b = input()
# str1= [0]*52
# str2 = [0]*52
# for x in a:
#     if x.isupper():
#         str1[ord(x)-65] +=1
#     else:
#         str1[ord(x)-71] +=1
#
# for x in a:
#     if x.isupper():
#         str2[ord(x) - 65] += 1
#     else:
#         str2[ord(x) - 71] += 1
#
# for i in range(len(str1)):
#     if str1[i] != str2[i]:
#         print("NO")
#         break
# else:
#     print("YES")

# if str1 == str2:
#     print("YES")
# else:
#     print("NO")
#


# '''개선 코드'''
# a = input()
# b = input()
# str= dict()
# for x in a:
#     str[x] = str.get(x,0) +1
# for x in b:
#     str[x] = str.get(x,0) -1
#
# for x in a:
#     if str.get(x) !=0:
#         print("NO")
#         break
# else:
#     print("YES")
#
# ''' 강의 풀이'''
# a = input()
# b = input()
# str1= dict()
# str2 = dict()
# # str1.get(x,0) x라는 값이 있으면 value를 아니면 0을 가져온다. getdefault ?
# for x in a:
#     str1[x] = str1.get(x,0) + 1
#
# for x in b:
#     str2[x] = str2.get(x,0) + 1
#
# for i in str1.keys():
#     if i in str2.keys():
#         if str1[i]!= str2[i]:
#             print("NO")
#             break
# else:
#     print("YES")