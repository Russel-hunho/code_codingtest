import sys
from itertools import combinations as cb
input = sys.stdin.readline
N,M = map(int,input().split())
numlist = list(map(int,input().split()))
combilist = list(cb(numlist,3))
print(combilist)
k = M
x = 0
state = 0
for i in combilist:
    if sum(i) == M:
        print(M)
        state = 1
        break
    elif sum(i) <= M and M-sum(i) < k:
        k = M-sum(i)
        x = sum(i)
if state == 0:
    print(x)
