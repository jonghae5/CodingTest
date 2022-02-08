
'''
강의 풀이
isdigit, isdecimal 둘 다 가능
'''
word = input()
res = 0
for word in word:
    if word.isdecimal():
        res = res * 10 + int(word)
cnt=0
for i in range(1,res+1):
    if res%i ==0:
        cnt+=1
print(res)
print(cnt)

''' 오종해 풀이'''

# word = input()
# number = ""
# for word in word:
#     try:
#         number+=str(int(word))
#     except ValueError:
#         continue
#
# result = int(number)
# cnt=2 #1과 본인
# for j in range(2,result//2+1):
#     if result%j ==0:
#         cnt+=1




