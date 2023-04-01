import sys
input = sys.stdin.readline

n = int(input())
nlist = []
for _ in range(n):
    templist = list(map(int,input().split()))
    nlist.append(templist)

DP = [[nlist[0][0]]]

for i in range(1,n):
    temp = []
    for j in range(i+1):
        if j == 0:
            temp.append(nlist[i][0]+DP[i-1][0])
        elif j == i:
            temp.append(nlist[i][i]+DP[i-1][i-1])
        else:
            temp.append(nlist[i][j] + max(DP[i-1][j-1:j+1]))
    DP.append(temp)

print(max(DP[n-1]))