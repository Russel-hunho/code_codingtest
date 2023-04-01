import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Nlist = list(map(int,input().split()))
for _ in range(M):
    i,j = map(int,input().split())
    print(sum(Nlist[i:j+1]))
    
## 시간초과 뜸
# 누적 합을 만들어두어 빼는 식으로, 반복을 줄이자!

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Nlist = list(map(int,input().split()))
Nsumstack = [Nlist[0]]
for i in range(len(Nlist)-1):
    Nsumstack.append( Nsumstack[i] + Nlist[i+1])
for _ in range(M):
    i,j = map(int,input().split())
    if i == 1:
        print(Nsumstack[j-1])
    else:
        print(Nsumstack[j-1]-Nsumstack[i-2])