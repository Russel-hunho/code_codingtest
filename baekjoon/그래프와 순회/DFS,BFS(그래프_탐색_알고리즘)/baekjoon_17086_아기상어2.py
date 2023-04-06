import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
shark = [list(map(int,input().split())) for i in range(N)]
safety = 0

dx = [1,1,1,0,-1,-1,-1,0]
dy = [-1,0,1,1,1,0,-1,-1]

for i in range(N):
    for j in range(M):
        if shark[i][j] == 0: # 상어가 아니라면
            que = deque([[i,j,0]])
            #방문처리
            visited = [[0]*M for i in range(N)]
            visited[i][j] = 1
            state = 1
            while que:
                a = que.popleft()
                ii = a[0]
                jj = a[1]
                depth = a[2]
                for k in range(8):
                    iii = ii + dx[k]
                    jjj = jj + dy[k]
                    if iii >= 0 and jjj >= 0 and iii < N and jjj < M:
                        if shark[iii][jjj] == 1: # 상어를 만나면
                            safety = max(safety,depth+1) #안전거리 입력하고 탈출
                            state = 0
                            break
                        if visited[iii][jjj] == 0:
                            visited[iii][jjj] = 1
                            que.append([iii,jjj,depth+1])
                if state == 0:
                    break
print(safety)

#pypy로 통과