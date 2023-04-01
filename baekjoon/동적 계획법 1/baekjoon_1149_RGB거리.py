import sys
input = sys.stdin.readline

N = int(input())
RGBlist = []
for i in range(N):
    RGB_i = list(map(int,input().split()))
    RGBlist.append(RGB_i)

DP = [[0,0,0]for i in range(N)]
#초기값
DP[0] = RGBlist[0]

for i in range(1,N):
    DP[i][0] = min(DP[i-1][1:3])+RGBlist[i][0]
    DP[i][1] = min(DP[i-1][0],DP[i-1][2])+RGBlist[i][1]
    DP[i][2] = min(DP[i-1][0:2])+RGBlist[i][2]

print(min(DP[N-1]))