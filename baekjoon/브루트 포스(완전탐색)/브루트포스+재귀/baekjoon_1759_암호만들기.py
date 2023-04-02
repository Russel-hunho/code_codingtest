import sys
from itertools import combinations as cb
input = sys.stdin.readline
L,C = map(int,input().split())
Clist = list(input().rstrip().split())
Clist.sort()
poss = cb(list(range(C)),L)

ans = []
for p in poss:
    mo = 0
    ja = 0
    code = ""
    for i in range(L):
        a = Clist[p[i]]
        code += a
        if a in ["a","e","i","o","u"]:
            mo += 1
        else:
            ja += 1
    if mo >= 1 and ja >= 2:
        ans.append(code)
#이미 sort되어있음
for i in ans:
    print(i)