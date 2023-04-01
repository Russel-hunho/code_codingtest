import sys
from collections import deque
input = sys.stdin.readline
M,N = map(int,input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

movexy = [[1,0],[0,1],[-1,0],[0,-1]]

def BFS(x,y,k):
    queue = deque([[x,y,0]])
    graph[x][y] = 2 #방문한 익은 토마토는 2로 처리
    global movexy
    while queue:
        v = queue.popleft()
        ix = v[0]
        iy = v[1]
        depth = v[2]
        for a in range(4):
            jx = ix + movexy[a][0]
            jy = iy + movexy[a][1]
            if (jx in range(N)) and (jy in range(M)):
                if graph[jx][jy] == 
        
        
    
    


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            k = 0
            BFS(i,j,k)