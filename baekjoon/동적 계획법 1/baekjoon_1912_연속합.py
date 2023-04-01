'''
import sys
input = sys.stdin.readline
n = int(input())
Alist = list(map(int,input().split()))
for i in Alist: #누적합
    Blist = [0]
    for j in range(n):
        Blist.append(Blist[-1]+Alist[j])
    #0 ~ n까지 n+1개

def maxi(B):
    k = 0
    for i in range(n):
        for j in range(i,n+1):
            k = max(k,B[j]-B[i])
    return k

print(maxi(Blist))

'''
# 시간초과
'''
import sys
input = sys.stdin.readline
n = int(input())
Alist = list(map(int,input().split()))
for i in Alist: #누적합
    Blist = [0]
    for j in range(n):
        Blist.append(Blist[-1]+Alist[j])
    #0 ~ n까지 n+1개

def maxi(B):
    k = max(B)-B[1]
    a = B[1]
    i = 1
    while True:
        if i >= len(B)-1:
            break
        i += 1
        if B[i] < a:
            a = B[i]
            k = max(k,max(B[i+1:])-a)
    return k

print(maxi(Blist))

'''
# 여전히 시간초과
## DP 이용!!

import sys
input = sys.stdin.readline
n = int(input())
Alist = list(map(int,input().split()))
#누적합
Blist = [Alist[0]]
for i in range(1,n):
    Blist.append(Blist[-1]+Alist[i])

DP1 = [0]*n # 정답 저장
DP2 = 0 # 누적합의 최솟값 저장
#초기값 setting
DP1[0] = Blist[0]
DP2 = min(0,Blist[0])

for i in range(1,n):
    DP1[i] = max( DP1[i-1], Blist[i]-DP2)
    DP2 = min(DP2, Blist[i])

print(DP1[n-1])