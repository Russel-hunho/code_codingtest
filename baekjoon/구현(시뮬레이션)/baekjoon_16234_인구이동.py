import sys
from collections import deque
input = sys.stdin.readline
N,L,R = map(int,input().split())

people = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for time in range(2000):    
    visited = [[0]*N for _ in range(N)]
    graphcount = 0
    sumgraph = [0]
    #인구이동 탐색
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                que = deque([[i,j]])
                graphcount += 1
                visited[i][j] = graphcount
                localsum = people[i][j]
                peoplecount = 1
                while que:
                    a = que.popleft()
                    ii = a[0]
                    jj = a[1]
                    for k in range(4):
                        iii = ii + dx[k]
                        jjj = jj + dy[k]
                        if iii >= 0 and jjj >= 0  and iii < N and jjj < N:
                            if visited[iii][jjj] == 0 and L <= abs(people[iii][jjj]-people[ii][jj]) <= R:
                                visited[iii][jjj] = graphcount
                                localsum += people[iii][jjj]
                                peoplecount += 1
                                que.append([iii,jjj])
                sumgraph.append(localsum//peoplecount)
    
    #인구이동 할 게 없다면
    if graphcount == N**2:
        print(time)
        exit(0)
    elif graphcount == 1:
        print(time+1)
        exit(0)
    #인구이동
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 0:
                people[i][j] = sumgraph[visited[i][j]]