'''
import sys
input = sys.stdin.readline
n = int(input())
s = list(input().rstrip()) # n*(n+1)/2개
# 답이 여러개일 수 있는데, 아무거나 출력하면 됨.
# n은 1~10
# a_i는 -10~10 -> 중복순열 만들어 처리하자!
from itertools import product as pd
anlist_product = pd(list(range(-10,11)),repeat = n)

for anlist in anlist_product:
    state = True
    sumanlist = [0] # 누적합
    for i in anlist:
        sumanlist.append(sumanlist[-1]+i)
    for i in range(n):
        for j in range(i,n):
            sumij = sumanlist[j+1]-sumanlist[i]
            sindex = i*(2*n-i+1)//2 + (j-i)
            if s[sindex] == "+" and sumij <= 0:
                state = False
                break
            if s[sindex] == "-" and sumij >= 0:
                state = False
                break
            if s[sindex] == "0" and sumij != 0:
                state = False
                break
        if state == False:
            break
    if state == True:
        for a in anlist:
            print(a, end=" ")
        break
'''

# 시간초과
'''
import sys
input = sys.stdin.readline
n = int(input())
s = list(input().rstrip()) # n*(n+1)/2개
# 답이 여러개일 수 있는데, 아무거나 출력하면 됨.
# n은 1~10
# a_i는 -10~10 -> 중복순열 만들어 처리하자!
from itertools import product as pd
anlist_product = pd(list(range(0,11)),repeat = n)

for anlist in anlist_product:
    state = True
    #불가능한경우 빠르게 제거하기
    for i in range(n):
        sindex = i*(2*n-i+1)//2
        if (s[sindex] in ["-","+"] and anlist[i] == 0) or (s[sindex] == "0" and anlist[i] != 0):
            state = False
            break
    if state == False:
        continue # 다음 탐색으로 가기
    
    #anlist의 부호 정하기
    anlist = [i for i in anlist] #튜플에서 list로 바꾸기
    for i in range(n):
        sindex = i*(2*n-i+1)//2
        if s[sindex] == "-":
            anlist[i] *= -1
    # 누적합 만들기
    sumanlist = [0] 
    for i in anlist:
        sumanlist.append(sumanlist[-1]+i)
    for i in range(n):
        for j in range(i,n):
            sumij = sumanlist[j+1]-sumanlist[i]
            sindex = i*(2*n-i+1)//2 + (j-i)
            if s[sindex] == "+" and sumij <= 0:
                state = False
                break
            if s[sindex] == "-" and sumij >= 0:
                state = False
                break
            if s[sindex] == "0" and sumij != 0:
                state = False
                break
        if state == False:
            break
    if state == True:
        for a in anlist:
            print(a, end=" ")
        break
'''

# 여전히 시간초과

'''
import sys
input = sys.stdin.readline
n = int(input())
s = list(input().rstrip()) # n*(n+1)/2개
# 답이 여러개일 수 있는데, 아무거나 출력하면 됨.
# n은 1~10
# a_i는 -10~10 -> 중복순열 만들어 처리하자!
siilist = []
zerocount = 0
for i in range(n):
    sindex = i*(2*n-i+1)//2
    sii = s[sindex]
    siilist.append(sii)
    if sii == "0":
        zerocount += 1

if zerocount == n: #싹다 0인경우
    for i in range(n):
        print(0, end=" ")
else:
    from itertools import product as pd
    anlist_product = pd(list(range(1,11)),repeat = n-zerocount) #0을 뺀 갯수만큼만
    for alist in anlist_product:
        #anlist 완성시키기
        anlist = []
        k = 0
        for i in range(n):
            if siilist[i] == "0":
                anlist.append(0)
            else:
                if siilist[i] == "-":
                    anlist.append((-1)*alist[k])
                else:
                    anlist.append(alist[k])
                k += 1
            
        state = True
        # 누적합 만들기
        sumanlist = [0] 
        for i in anlist:
            sumanlist.append(sumanlist[-1]+i)
        for i in range(n):
            for j in range(i,n):
                sumij = sumanlist[j+1]-sumanlist[i]
                sindex = i*(2*n-i+1)//2 + (j-i)
                if s[sindex] == "+" and sumij <= 0:
                    state = False
                    break
                if s[sindex] == "-" and sumij >= 0:
                    state = False
                    break
                if s[sindex] == "0" and sumij != 0:
                    state = False
                    break
            if state == False:
                break
        if state == True:
            for a in anlist:
                print(a, end=" ")
            break
'''

# array를 만들어 index 계산을 줄여보자!
'''
import sys
input = sys.stdin.readline
n = int(input())
s = list(input().rstrip()) # n*(n+1)/2개
# 답이 여러개일 수 있는데, 아무거나 출력하면 됨.
# n은 1~10
# a_i는 -10~10 -> 중복순열 만들어 처리하자!

sarray = [[0]*n for i in range(n)]
k = 0
for i in range(n):
    for j in range(i,n):
        sarray[i][j] = s[k]
        k += 1

siilist = [sarray[i][i] for i in range(n)]
zerocount = siilist.count(0)

if zerocount == n: #싹다 0인경우
    for i in range(n):
        print(0, end=" ")
else:
    from itertools import product as pd
    anlist_product = pd(list(range(1,11)),repeat = n-zerocount) #0을 뺀 갯수만큼만
    for alist in anlist_product:
        #anlist 완성시키기
        anlist = []
        k = 0
        for i in range(n):
            if siilist[i] == "0":
                anlist.append(0)
            else:
                if siilist[i] == "-":
                    anlist.append((-1)*alist[k])
                else:
                    anlist.append(alist[k])
                k += 1
            
        state = True
        # 누적합 만들기
        sumanlist = [0] 
        for i in anlist:
            sumanlist.append(sumanlist[-1]+i)
        for i in range(n):
            for j in range(i+1,n):
                sumij = sumanlist[j+1]-sumanlist[i]
                if sarray[i][j] == "+" and sumij <= 0:
                    state = False
                    break
                if sarray[i][j] == "-" and sumij >= 0:
                    state = False
                    break
                if sarray[i][j] == "0" and sumij != 0:
                    state = False
                    break
            if state == False:
                break
        if state == True:
            for a in anlist:
                print(a, end=" ")
            break
'''


## 계속 시간초과.. 안된다... 백트래킹으로 풀어야 함!


import sys
input = sys.stdin.readline
n = int(input())
s = list(input().rstrip()) # n*(n+1)/2개
# 답이 여러개일 수 있는데, 아무거나 출력하면 됨.
# n은 1~10
# a_i는 -10~10

sarray = [[0]*n for i in range(n)]
k = 0
for i in range(n):
    for j in range(i,n):
        sarray[i][j] = s[k]
        k += 1
# 다음 경우의 수 만드는 함수
def appendnext(k,aklist):
    global sarray
    global n
    if test(k,aklist) == False:
        return False
    # True인 경우
    if k == n:
        print(" ".join([str(i) for i in aklist]))
        exit(0) #아예 종료
    if sarray[k][k] == "0":
        appendnext(k+1,aklist+[0])
    elif sarray[k][k] == "+":
        for i in range(1,11):
            appendnext(k+1,aklist+[i])
    else:
        for i in range(-1,-11,-1):
            appendnext(k+1,aklist+[i])

def test(k,aklist): # aklist엔 k개의 원소가 들어가있고, k번째 원소가 막 추가된 경우에서 확인
    global n
    global sarray
    if k == 0:
        return True
    for i in range(k-1): 
        sumaik = sum(aklist[i:])
        if sarray[i][k-1] == "+" and sumaik <= 0:
            return False
        if sarray[i][k-1] == "-" and sumaik >= 0:
            return False
        if sarray[i][k-1] == "0" and sumaik != 0:
            return False
    return True

appendnext(0,[])
