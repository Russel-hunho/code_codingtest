import sys
input = sys.stdin.readline
N,M = map(int,input().split())

table = []
visited = [ [[0,0] for j in range(M)] for i in range(N) ]
    #https://kscodebase.tistory.com/66
    #x,y 외에, 방문시에 벽 부순 기록 여부를 기록
        #visited[x][y] = [state1,state2]
            #state1: 벽 안부수고 방문한 이력의 depth 기록
            #state2: 벽 부수고 방문한 이력의 depth 기록
visited[0][0][0] = 1
for i in range(N):
    table.append([int(i) for i in list(input().rstrip())])

from collections import deque
que = deque([[0,0,1,0]])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
while que:
    a = que.popleft()
    x = a[0]
    y = a[1]
    depth = a[2]
    s = a[3] # 벽 부순 이력 여부
    for i in range(4):
        xi = x+dx[i]
        yi = y+dy[i]
        if xi>=0 and xi<N and yi>=0 and yi<M:
            if table[xi][yi] == 0: #벽이 아니라면
                if visited[xi][yi][s] == 0 or visited[xi][yi][s] > depth+1:
                    #방문기록이 없었거나, 현 방문보다 경로가 길었다면
                    visited[xi][yi][s] = depth+1
                    que.append([xi,yi,depth+1,s])
            elif s == 0: # 벽이고 부순 기록이 없다면
                if visited[xi][yi][1] == 0 or visited[xi][yi][1] > depth+1:
                    visited[xi][yi][1] = depth+1
                    que.append([xi,yi,depth+1,1])
if visited[N-1][M-1] == [0,0]:
    print(-1)
elif min(visited[N-1][M-1]) == 0:
    print(max(visited[N-1][M-1]))
else:
    print(min(visited[N-1][M-1]))