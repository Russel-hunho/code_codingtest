'''
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
A = [] # 격자판
for _ in range(N):
    A.append(list(map(int,input().split())))

from itertools import combinations as cb
NM = [i for i in range(N*M)]
    #i번째 index: A[i//M][i%M] (0~N-1)(0~M-1)
B = list(cb(NM,K))
    #0~(N*M-1) 중 K개를 선택한 조합
klist = list(cb(list(range(K)),2))
    #B의 원소 b(K개의 원소)에서 0~K-1까지 중 2개 비교를 위함
C = []
    #인접이 없는 B의 원소 b만 담기 위함
for b in B:
    state = 0
    for i in klist:
        x = b[i[0]]
        y = b[i[1]]
        if abs(x-y) == M: #상하인접
            state = 1
        if abs(x-y) == 1 and x//M == y//M: #좌우인접
            state = 1
    if state == 0:
        C.append(b)
Ans = 0
for c in C:
    sumA = 0
    for i in c:
        sumA += A[i//M][i%M]
    Ans = max(Ans,sumA)
print(Ans)
'''

# 시간초과 --> pypy로는 통과!


import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
A = [] # 격자판
for _ in range(N):
    A.append(list(map(int,input().split())))

if K == 1:
    maxA = -10000
    for i in range(N):
        maxA = max(maxA,max(A[i]))
    print(maxA)
else:
    from itertools import combinations as cb
    NM = [i for i in range(N*M)]
        #i번째 index: A[i//M][i%M] (0~N-1)(0~M-1)
    B = list(cb(NM,K))
        #0~(N*M-1) 중 K개를 선택한 조합

    Ans = -40000
    for b in B:
        state = 0
        for i in cb(list(range(K)),2):
                #B의 원소 b(K개의 원소)에서 0~K-1까지 중 2개 비교를 위함
            x = b[i[0]]
            y = b[i[1]]
            if abs(x-y) == M: #상하인접
                state = 1
            if abs(x-y) == 1 and x//M == y//M: #좌우인접
                state = 1
        if state == 0:
            sumA = 0
            for i in b:
                sumA += A[i//M][i%M]
            Ans = max(Ans,sumA)

    print(Ans)