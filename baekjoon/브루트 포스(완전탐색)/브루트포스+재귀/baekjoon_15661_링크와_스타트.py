import sys
input = sys.stdin.readline
N = int(input())
from itertools import combinations as cb
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))
    
comb = []
for k in range(1,N-1):
    comb += list(cb(list(range(N-1)),k)) # N (index로는 N-1)이 속하지 않은 경우의 수들
ans = 10**9
for comb1 in comb:
    comb2 = list(set(list(range(N)))-set(comb1)) # N이 속한 집합
    power = 0
    if len(comb1) != 1:
        for a in comb1:
            for b in comb1:
                power += A[a][b]
    if len(comb2) != 1:
        for a in comb2:
            for b in comb2:
                power -= A[a][b]
    ans = min(ans,abs(power))
    if ans == 0:
        break
print(ans)

## pypy로 통과