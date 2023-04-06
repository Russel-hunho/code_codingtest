import sys
from collections import deque
N = int(input())
pic_RGB = []
pic_GGB = []
for _ in range(N):
    Nlist = list(input().rstrip())
    pic_RGB.append(Nlist)
    temp_GGB = []
    for i in Nlist:
        if i != "B":
            temp_GGB.append("G")
        else:
            temp_GGB.append("B")
    pic_GGB.append(temp_GGB)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def BFS(pic):
    global N,dx,dy
    visited = [[0]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0: #방문 전이라면
                visited[i][j] = 1 #방문처리
                count += 1
                groupcolor = pic[i][j]
                que = deque([[i,j]])
                while que:
                    a = que.popleft()
                    ii = a[0]
                    jj = a[1]
                    for k in range(4):
                        iii = ii + dx[k]
                        jjj = jj + dy[k]
                        if iii >= 0 and iii < N and jjj >= 0 and jjj < N:
                            if visited[iii][jjj] == 0 and pic[iii][jjj] == groupcolor:
                                que.append([iii,jjj])
                                visited[iii][jjj] = 1 # 방문처리
    return count
    
print(BFS(pic_RGB),BFS(pic_GGB))