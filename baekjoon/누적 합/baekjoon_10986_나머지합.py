'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Alist = list(map(int,input().split()))

#초기값 세팅
count = 0
Sumlist = []
for i in Alist:
    if i%M == 0:
        count += 1
    Sumlist.append(i)
#1개의 합은 끝
for i in range(2,N+1):
    #i: 연속된 i개의 합을 의미
    for j in range(N-i+1):
        k = (Sumlist[j] + Alist[i+j-1]) % M
            #Sumlist에는 i-1개의 합이 저장되어있는 상태
            #index기준 j부터 j+i-2까지
        if k == 0:
            count += 1
        Sumlist[j] = k
print(count)
'''

## 시간초과

'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Alist = list(map(int,input().split()))

#초기값 세팅
count = 0
Sumlist = [Alist[0]]
for i in range(N-1):
    Sumlist.append( Sumlist[i] + Alist[i+1] )


for i in range(N):
    for j in range(i+1,N):
        if ( Sumlist[j] - Sumlist[i] ) % M == 0:
            count += 1
    if Sumlist[i]%M == 0:
        count += 1
print(count)
'''
#여전히 시간초과

## O(N+M)으로 푸는 법 ##
# https://www.acmicpc.net/board/view/34308

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Alist = list(map(int,input().split()))

Mdict = dict() # 누적합의 나머지: 나온 횟수
k = Alist[0]%M
Mdict[k] = 1
for i in range(1,N):
    k = (k + Alist[i])%M
    if k in Mdict.keys():
        Mdict[k] += 1
    else:
        Mdict[k] = 1

count = 0
for i in Mdict.keys():
    if i == 0:
        count += Mdict[i]
    count += Mdict[i]*(Mdict[i]-1)//2
print(count)