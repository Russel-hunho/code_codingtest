##5622   다이얼

X = list(str(input())) ## 한 문자씩 list에 저장
num = 0
for i in range(len(X)):
    if ord(X[i]) < 83: #65~67: A,B,C : 2 : 3초
        num += int( ( ord(X[i])-65 ) / 3 ) + 3
    elif ord(X[i]) < 90: #83~89
        num += int( ( ord(X[i])-66 ) / 3 ) + 3
    else:
        num += 10
print(num)


##2941   크로아티아 알파벳
X = list(str(input()))
num = len(X)
for i in range(1,len(X)):
    if X[i] == "-":
        num -= 1
    elif X[i] == "=":
        if i > 1 and X[i-1] == "z" and X[i-2] == "d":
            num -= 2
        else: 
            num -= 1
    elif X[i] == "j" and i > 0:
        if X[i-1] == "l" or X[i-1] == "n":
            num -= 1
print(num)


##1316   그룹 단어 체크
import sys
N = int(input())
for i in range(N):
    X = list(str(sys.stdin.readline()))

# 노말한 버전
N = int(input())
num = 0
for i in range(N):
    X = list(str(input()))
    setnum = len(set(X))
    count = 1
    for j in range(1,len(X)):
        if X[j] != X[j-1]:
            count += 1
    if count == setnum:
        num += 1
print(num)
    
    
    