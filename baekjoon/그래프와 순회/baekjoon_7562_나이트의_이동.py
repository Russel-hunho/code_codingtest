import sys
input = sys.stdin.readline
from collections import deque
T = int(input())

movexy = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

def BFS(graph,I, x,y, tx, ty):
    queue = deque([[x,y,0]])
    graph[x][y] = True # 방문 표시 for 중복 제거
    global movexy
    while queue:
        v = queue.popleft()
        ix = v[0]
        iy = v[1]
        depth = v[2]
        #타겟 위치에 있으면 종료
        if ix == tx and iy == ty:
            print(depth)
            break
        #타겟 위치가 아니면 다음 depth 탐색
        depth += 1
        for a in range(8):
            jx = ix + movexy[a][0]
            jy = iy + movexy[a][1]
            if ( jx in range(0,I) ) and ( jy in range(0,I) ):
                if graph[jx][jy] == False:
                    queue.append([jx,jy,depth])
                    graph[jx][jy] = True
    return 0

for _ in range(T):
    I = int(input())
    x,y = map(int,input().split())
    tx, ty = map(int,input().split())
    graph = [[False]*I for i in range(I)]
    BFS(graph,I,x,y,tx,ty)
