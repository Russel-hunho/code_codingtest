import sys
from itertools import permutations as pm
input = sys.stdin.readline
k = int(input())
klist = [i for i in range(10)] # 0부터9까지
boo = list(input().rstrip().split()) # k개

ans = []
A = list(pm(klist,k+1))
for a in A:
    state = True
    for i in range(k):
        if boo[i] == ">":
            if a[i] < a[i+1]:
                state = False
                break
        if boo[i] == "<":
            if a[i] > a[i+1]:
                state = False
                break
    if state == True:
        anum = "".join([str(i) for i in a])
        ans.append(anum)
ans.sort()
print(ans[-1])
print(ans[0])