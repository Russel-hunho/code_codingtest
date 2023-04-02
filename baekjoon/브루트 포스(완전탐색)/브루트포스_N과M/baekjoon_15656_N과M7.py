import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Nlist = list(map(int,input().split()))
Nlist.sort()
from itertools import product as pd
A = list(pd(Nlist,repeat = M))
for a in A:
    for i in range(M):
        print(a[i], end = " ")
    print()