import sys
input = sys.stdin.readline
n = int(input())
nlist = []
for _ in range(n):
    nlist.append(int(input()))

if n <= 2:
    print(sum(nlist))
else:
    DP = [0]*(n+1)
    DP[0:3] = [0, nlist[0], sum(nlist[0:2])]
    for j in range(3, n+1):
        DP[j] = nlist[j-1] + max(DP[j-2], (max(DP[0:j-2])+nlist[j-2]))
    print(max(DP))