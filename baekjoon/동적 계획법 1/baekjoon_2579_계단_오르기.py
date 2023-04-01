import sys
input = sys.stdin.readline

n = int(input())
nlist = []
for _ in range(n):
    nlist.append(int(input()))

if n <= 2:
    print(sum(nlist))
elif n == 3:
    print(max(nlist[0:2])+nlist[2])
else:
    DP = [0,nlist[0],sum(nlist[0:2]), max(nlist[0:2])+nlist[2]] #DP[0]~DP[3] (0, x[0], x[0]+x[1], 3의 최적값)
    for i in range(4,n+1):
        DP.append( nlist[i-1] + max(DP[i-2], DP[i-3]+nlist[i-2]) )
    print(DP[n])
    