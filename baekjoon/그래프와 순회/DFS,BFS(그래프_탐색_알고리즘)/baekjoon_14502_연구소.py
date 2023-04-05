import sys
from collections import deque
from itertools import combinations as cb
input = sys.stdin.readline
N,M = map(int,input().split())
table = []
zero_location = [] # 브루트포스 적용
for i in range(N):
    Mlist = list(map(int,input().split()))
    table.append(Mlist)
    for j in range(M):
        if Mlist[j] == 0:
            zero_location.append([i,j])

ans = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(table):
    global dx,dy, N,M
    
    #다 탐색하며 감염시키기
    for i in range(N):
        for j in range(M):
            if table[i][j] == 2:
                table[i][j] = 3 #방문처리
                que = deque([[i,j]])
                while que:
                    a = que.popleft()
                    x = a[0]
                    y = a[1]
                    for k in range(4):
                        x1 = x + dx[k]
                        y1 = y + dy[k]
                        if 0 <= x1 and N > x1 and 0 <= y1 and M > y1:
                            if table[x1][y1] in (0,2):
                                table[x1][y1] = 3 #방문한 바이러스 처리
                                que.append([x1,y1]) # 추가감염 탐색
    count = 0 #생존 영역 세기
    for i in range(N):
        for j in range(M):
            if table[i][j] == 0:
                count += 1
    return count                   

zero_brute = list(cb(zero_location,3)) #리스트의 원소: 튜플, ([i1,j1],[i2,j2],[i3,j3])
for z in zero_brute:
    localtable = []
    #table 복사
    for i in range(N):
        temp = []
        for j in range(M):
            temp.append(table[i][j])
        localtable.append(temp)
    #벽세우기
    zi1,zj1 = z[0][0],z[0][1]
    zi2,zj2 = z[1][0],z[1][1]
    zi3,zj3 = z[2][0],z[2][1]
    localtable[zi1][zj1] = 1
    localtable[zi2][zj2] = 1
    localtable[zi3][zj3] = 1
    #BFS탐색
    ans = max(ans,bfs(localtable))
print(ans)