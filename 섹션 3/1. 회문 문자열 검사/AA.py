n = int(input())
''' 
정석 풀이
면접에서는 이게 더 유용하다. 
'''
for i in range(n):
    lang = str(input())
    lang = lang.upper()
    size = len(lang)
    for j in range(size//2):
        num_st = j
        if lang[num_st] != lang[-1-num_st]:
            print('#{} NO'.format(i+1))
            break
    else:
        print('#{} YES'.format(i+1))

'''
강의 풀이
파이썬 스러운 코드
'''
# for i in range(n):
#     s = input()
#     s = s.upper()
#     if s ==s[::-1]:
#         print('#{} Yes'.format(i + 1))
#     else:
#         print('#{} NO'.format(i + 1))