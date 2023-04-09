import sys
input = sys.stdin.readline
from collections import deque
R,C,T = map(int,input().split())
A = []
for i in range(R):
    x = list(map(int,input().split()))
    if x[0] == -1:
        poss = i
    A.append(x)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
poss2 = poss
poss1 = poss-1

def misae(A):
    global R,C, poss1, poss2
    B = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if A[r][c] > 0: # 0, -1 제외
                count = 0
                klist = []
                #확산가능여부 탐색
                for k in range(4):
                    rk = r + dx[k]
                    ck = c + dy[k]
                    if 0<=rk<R and 0<=ck<C: # 벽이 아니고
                        if A[rk][ck] != -1: # 공기청소기가 아니면
                            count += 1
                            klist.append(k)
                #확산
                B[r][c] += A[r][c] - (A[r][c]//5)*count
                for k in klist:
                    rk = r + dx[k]
                    ck = c + dy[k]
                    B[rk][ck] += A[r][c]//5
    B[poss1][0] = -1
    B[poss2][0] = -1
    return B

def air(A):
    global R,C,poss1,poss2
    B = [[0]*C for _ in range(R)]
    #poss1 확산
    for r in range(R):
        for c in range(C):
            if r == 0:
                if c < C-1:
                    B[r][c] = A[r][c+1]
                else:
                    B[r][c] = A[r+1][c]
            elif r in [poss1,poss2]:
                if c == 0:
                    B[r][c] = -1 # 공기청정기 유지
                elif c == 1:
                    B[r][c] = 0 # 깨끗한 바람 나옴
                else:
                    B[r][c] = A[r][c-1]
            elif r == R-1:
                if c < C-1:
                    B[r][c] = A[r][c+1]
                else:
                    B[r][c] = A[r-1][c]
            elif (c == 0 and r < poss1) or (c == C-1 and r > poss2):
                #아래로 내리기
                B[r][c] = A[r-1][c]
            elif (c == 0 and r > poss2) or (c == C-1 and r < poss1):
                #위로 올리기
                B[r][c] = A[r+1][c]
            else:
                B[r][c] = A[r][c]
    return B

for _ in range(T):
    A = misae(A)
    A = air(A)


ans = 0
for i in range(R):
    ans += sum(A[i])
print(ans+2) #공기청정기 -1 두칸 보상

