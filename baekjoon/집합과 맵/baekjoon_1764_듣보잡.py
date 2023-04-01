'''import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Nlist = []
totlist = []
for _ in range(N):
    Nlist.append(input().rstrip())
for _ in range(M):
    k = input().rstrip()
    if k in Nlist:
        totlist.append(k)
print(len(totlist))
for i in totlist:
    print(i)'''
    
##역시나 in 함수로 List 탐색은 시간초과
# set 만들어서 해보자

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Nlist = []
Mlist = []
Nset = {}
Mset = {}

for _ in range(N):
    Nlist.append(input().rstrip())
for _ in range(M):
    Mlist.append(input().rstrip())
Nset = set(Nlist)
Mset = set(Mlist)
totset = Nset & Mset
print(len(totset))
for i in sorted(totset):
    print(i)