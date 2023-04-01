##itertools 이용
from itertools import combinations_with_replacement as cb_with_rep

N,M = map(int,input().split())
A = list(range(1,N+1))
B = list(cb_with_rep(A,M))
for X in B:
    for i in X:
        print(i, end = " ")
    print()


## 탐색 이용
N,M = map(int,input().split())
A = [[i] for i in range(1,N+1)]
B = [[i] for i in range(1,N+1)]

def f(C,i):
    if i == 1:
        return C
    temp = []
    for j in C:
        for k in A:
            if k[0] >= j[-1]:
                temp.append(j+k)
    C = temp
    return f(C,i-1)

K = f(B,M)
for x in K:
    for i in x:
        print(i, end = " ")
    print()
