import sys
from itertools import permutations as pm
input = sys.stdin.readline
N = int(input())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))
# 차례대로 + - X / 개수 & 총합은 N-1개
Clist = ["+"]*Blist[0] + ["-"]*Blist[1] + ["*"]*Blist[2] + ["/"]*Blist[3]
maxi = -10**9
mini = 10**9

Dlist = list(pm(Clist,N-1))

for X in Dlist:
    Ans = Alist[0]
    for i in range(N-1):
        if X[i] == "+":
            Ans += Alist[i+1]
        elif X[i] == "-":
            Ans -= Alist[i+1]
        elif X[i] == "*":
            Ans *= Alist[i+1]
        else :
            Ans = int(Ans/Alist[i+1])
                ##음수 나눗셈 룰 주의!
    maxi = max(maxi,Ans)
    mini = min(mini,Ans)
print(maxi)
print(mini)

##시간초과 (pypy3로는 통과)


