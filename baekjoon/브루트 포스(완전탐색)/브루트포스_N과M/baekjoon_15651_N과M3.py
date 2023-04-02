N,M = map(int,input().split())
Nlist = [i+1 for i in range(N)]
from itertools import product as pd
A = list(pd(Nlist,repeat = M))
for a in A:
    for i in range(M):
        print(a[i], end = " ")
    print()