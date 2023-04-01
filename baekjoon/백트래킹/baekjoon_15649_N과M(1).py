from itertools import permutations as pm
from itertools import combinations as cb
from itertools import combinations_with_replacement as cb_with_re
from itertools import product as pd

N,M = map(int,input().split())
A = list(range(1,N+1))

## 중복조합
B = list(pm(A,M))
B.sort()
for i in B:
    for j in i:
        print(j, end = " ")
    print()

print()

## 순열조합
B = list(cb(A,M))
B.sort()
for i in B:
    for j in i:
        print(j, end = " ")
    print()

print()

## 
B = list(cb_with_re(A,M))
B.sort()
for i in B:
    for j in i:
        print(j, end = " ")
    print()
    

print()

B = list(pd(A,A,repeat = M))
B.sort()
for i in B:
    for j in i:
        print(j, end = " ")
    print()