import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Nlist = list(map(int,input().split()))
Nlist.sort()
from itertools import combinations as cb
A = list(cb(Nlist,M))
    # Nlist에 중복이 있어도, 다른 수라고 인식하고 만든다..!
#중복제거
A = list(set(A)) # 중복 제거
#set으로 제거하면, 순서 정렬 다시 해줘야함!
A.sort()
for a in A:
    for i in range(M):
        print(a[i], end=" ")
    print()