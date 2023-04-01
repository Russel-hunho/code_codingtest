N = int(input())
DP = [[0,1,1,1,1,1,1,1,1,1]] #1~9만 가능
for i in range(1,N):
    temp = []
    for j in range(10):
        if j == 0:
            temp.append(DP[i-1][1])
        elif j == 9:
            temp.append(DP[i-1][8])
        else:
            temp.append( (DP[i-1][j-1]+DP[i-1][j+1]) % 1000000000 )
    DP.append(temp)
print(sum(DP[N-1])%1000000000)