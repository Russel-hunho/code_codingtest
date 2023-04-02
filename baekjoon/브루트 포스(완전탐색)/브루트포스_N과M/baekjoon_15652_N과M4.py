N,M = map(int,input().split())
Nlist = [i+1 for i in range(N)]
from itertools import combinations_with_replacement as cbr
A = list(cbr(Nlist,M))
for a in A:
    for i in range(M):
        print(a[i], end = " ")
    print()