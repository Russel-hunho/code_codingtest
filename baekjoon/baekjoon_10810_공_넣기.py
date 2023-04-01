import sys
N,M = map(int,input().split())
Ans = [0 for j in range(N)]
for a in range(M):
    i,j,k = map(int,sys.stdin.readline().split())
    for b in range(i-1,j):
        Ans[b] = k
for a in Ans:
    print(a,end=" ")

##
N,M = map(int,input().split())
Ans = [0 for j in range(N)]
for _ in range(M):
    i,j,k = map(int,input().split())
    for b in range(i-1,j):
        Ans[b] = k
for a in Ans:
    print(a,end=" ")