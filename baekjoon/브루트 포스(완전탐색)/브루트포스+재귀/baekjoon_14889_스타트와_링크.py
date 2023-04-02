import sys
input = sys.stdin.readline
N = int(input())
from itertools import combinations as cb
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))
comb = list(cb(list(range(N-1)),N//2)) # N (index로는 N-1)이 속하지 않은 경우의 수들
ans = 10**9
for comb1 in comb:
    comb2 = list(set(list(range(N)))-set(comb1)) # N이 속한 집합
    power1 = 0
    power2 = 0
    cb1 = list(cb(comb1,2))
    cb2 = list(cb(comb2,2))
    for a in cb1:
        i = a[0]
        j = a[1]
        power1 += A[i][j]+A[j][i]
    for a in cb2:
        i = a[0]
        j = a[1]
        power2 += A[i][j]+A[j][i]
    ans = min(ans,abs(power1-power2))
print(ans)