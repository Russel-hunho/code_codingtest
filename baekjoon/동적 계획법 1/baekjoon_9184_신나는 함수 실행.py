import sys
input = sys.stdin.readline

# DP cache 지정
DP = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]
    #3차원 (0~20): 21*21*21: DP[0][0][0]~DP[20][20][20]
# 초기값 setting
for i in range(21):
    for j in range(21):
        DP[i][j][0] = 1
        DP[0][i][j] = 1
        DP[j][0][i] = 1

for a in range(1,21):
    for b in range(1,21):
        for c in range(1,21):
            if a>=b or b>=c:
                DP[a][b][c] = DP[a-1][b][c] + DP[a-1][b-1][c] + DP[a-1][b][c-1] - DP[a-1][b-1][c-1]
            else:
                DP[a][b][c] = DP[a][b][c-1] + DP[a][b-1][c-1] - DP[a][b-1][c]

while True:
    A = list(map(int,input().split()))
    if A == [-1, -1, -1]:
        break
    if A[0] <= 0 or A[1] <= 0 or A[2] <= 0:
        B = 1
    elif A[0] > 20 or A[1] > 20 or A[2] > 20:
        B = DP[20][20][20]
    else:
        B = DP[A[0]][A[1]][A[2]]
    print("w({}, {}, {}) = {}".format(A[0],A[1],A[2],B))