import sys
input = sys.stdin.readline
from itertools import combinations as cb

N = int(input())
statarray = []
for i in range(N):
    statarray.append(list(map(int,input().split())))

k = N//2
A = list(range(0,N))
B = list(range(0,N-1)) # N 제외
C = list(cb(B,k)) #N이 없는 팀의 경우의수들

mindelstat = 100*(k**2)
for X in C:
    Xstat = 0
    Ystat = 0
    Y = list(set(A)-set(X))
    for i in X:
        for j in X:
            Xstat += statarray[i][j]
    for i in Y:
        for j in Y:
            Ystat += statarray[i][j]
    delstat = abs(Xstat-Ystat)
    mindelstat = min(mindelstat,delstat)

print(mindelstat)