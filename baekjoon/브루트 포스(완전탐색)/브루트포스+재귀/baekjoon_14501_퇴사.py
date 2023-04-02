import sys
input = sys.stdin.readline
N = int(input())
Nlist = []
for _ in range(N):
    T,P = map(int,input().split())
    Nlist.append([T,P])

dp = [0]*(N+1)
for i in range(N,0,-1): #i일 탐색
    if Nlist[i-1][0] + i - 1 >= N+1:
        continue #그대로 0
    elif Nlist[i-1][0] + i - 1 == N:
        dp[i] = Nlist[i-1][1]
    else:
        dp[i] = Nlist[i-1][1] + max(dp[Nlist[i-1][0]+i:])
print(max(dp))