'''

import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())

table = []
visited = [ [[[0,0] for k in range(K+1)] for j in range(M)] for i in range(N) ]
visited[0][0][0][0] = 1 # 낮 시작
for i in range(N):
    table.append([int(i) for i in list(input().rstrip())])

from collections import deque
que = deque([[0,0,1,0,0]])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
while que:
    a = que.popleft()
    x = a[0]
    y = a[1]
    depth = a[2]+1 #다음 경로 (다음 이동의 depth)
    s = a[3] # 벽 부순 이력 여부
    daynight = 1-a[4] #낮/밤 바뀜 (다음 이동의 낮/밤 상태)
    for i in range(4):
        #다음이동 위치
        xi = x+dx[i]
        yi = y+dy[i]
        if xi>=0 and xi<N and yi>=0 and yi<M:
            if table[xi][yi] == 0: #벽이 아니라면
                if visited[xi][yi][s][daynight] == 0 or visited[xi][yi][s][daynight] > depth:
                    #방문기록이 없었거나, 현 방문보다 경로가 길었다면
                    visited[xi][yi][s][daynight] = depth
                    que.append([xi,yi,depth,s,daynight])
            elif s < K: # 벽이고 부순 기록이 K보다 적다면
                if daynight == 1: #낮 -> 다음 이동이 밤이 되는 상황
                    if visited[xi][yi][s+1][daynight] == 0 or visited[xi][yi][s+1][daynight] > depth:
                        visited[xi][yi][s+1][daynight] = depth
                        que.append([xi,yi,depth,s+1,daynight])
                else: #밤 -> 다음 이동이 낮이 되는 상황
                    if visited[xi][yi][s+1][1-daynight] == 0 or visited[xi][yi][s+1][1-daynight] > depth+1: #낮이 되길 기다려야함
                        visited[xi][yi][s+1][1-daynight] = depth+1 #낮이 된 다음 이동
                        que.append([xi,yi,depth+1,s+1,1-daynight])
if visited[N-1][M-1] == [[0,0]]*(K+1):
    print(-1)
else:
    ans = 10**7
    for i in range(K+1):
        for j in range(2):
            if visited[N-1][M-1][i][j] != 0:
                ans = min(visited[N-1][M-1][i][j],ans)
    print(ans)
    
'''

# 시간초과

'''
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())

table = []
visited = [ [[[10**7]*(K+1) for k in range(2)] for j in range(M)] for i in range(N) ]
visited[0][0][0][0] = 1 # 낮 시작
for i in range(N):
    table.append([int(i) for i in list(input().rstrip())])

from collections import deque
que = deque([[0,0,1,0,0]])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
while que:
    a = que.popleft()
    x = a[0]
    y = a[1]
    depth = a[2]+1 #다음 경로 (다음 이동의 depth)
    daynight = 1-a[3] #낮/밤 바뀜 (다음 이동의 낮/밤 상태)
    s = a[4] # 벽 부순 이력 여부
    for i in range(4):
        #다음이동 위치
        xi = x+dx[i]
        yi = y+dy[i]
        if xi>=0 and xi<N and yi>=0 and yi<M:
            if table[xi][yi] == 0: #벽이 아니라면
                if min(visited[xi][yi][daynight][0:s+1]) > depth: #greedy 적용
                    #방문기록이 없었거나, 현 방문보다 경로가 길었다면
                    visited[xi][yi][daynight][s] = depth
                    que.append([xi,yi,depth,daynight,s])
            elif s < K: # 벽이고 부순 기록이 K보다 적다면
                if daynight == 1: #낮 -> 다음 이동이 밤이 되는 상황
                    if min(visited[xi][yi][daynight][0:s+2]) > depth:
                        visited[xi][yi][daynight][s+1] = depth
                        que.append([xi,yi,depth,daynight,s+1])
                else: #밤 -> 다음 이동이 낮이 되는 상황
                    if min(visited[xi][yi][1-daynight][0:s+2]) > depth+1: #낮이 되길 기다려야함
                        visited[xi][yi][1-daynight][s+1] = depth+1 #낮이 된 다음 이동
                        que.append([xi,yi,depth+1,1-daynight,s+1])

ans = 10**7
for i in range(2):
    ans = min(min(visited[N-1][M-1][i]),ans)
if ans == 10**7:
    print(-1)
else:
    print(ans)
'''

#여전히 시간초과
# 낮/밤 구분을 그냥 depth의 홀/짝으로 생각하자!
'''
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())

table = []
visited = [ [[10**7]*(K+1) for j in range(M)] for i in range(N) ]
visited[0][0][0] = 1 # 낮 시작, #낮 = 홀수깊이
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
    depth = a[2]+1 #다음 경로 (다음 이동의 depth)
    s = a[3] # 벽 부순 이력 여부
    for i in range(4):
        #다음이동 위치
        xi = x+dx[i]
        yi = y+dy[i]
        if xi>=0 and xi<N and yi>=0 and yi<M:
            if table[xi][yi] == 0: #벽이 아니라면
                if min(visited[xi][yi][0:s+1]) > depth: #greedy 적용
                    #방문기록이 없었거나, 현 방문보다 경로가 길었다면
                    visited[xi][yi][s] = depth
                    que.append([xi,yi,depth,s])
            elif s < K: # 벽이고 부순 기록이 K보다 적다면
                if depth%2 == 0: #밤 -> 다음 이동이 밤이 되는 상황
                    if min(visited[xi][yi][0:s+2]) > depth:
                        visited[xi][yi][s+1] = depth
                        que.append([xi,yi,depth,s+1])
                else: #낮 -> 다음 이동이 낮이 되는 상황
                    if min(visited[xi][yi][0:s+2]) > depth+1: #낮이 되길 기다려야함
                        visited[xi][yi][s+1] = depth+1 #낮이 된 다음 이동
                        que.append([xi,yi,depth+1,s+1])

ans = min(visited[N-1][M-1])
if ans == 10**7:
    print(-1)
else:
    print(ans)
'''

#여전히 시간초과
#도착시 남은 탐색을 안하고 바로 멈추게끔 하자!
'''
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())

table = []
visited = [ [[10**7]*(K+1) for j in range(M)] for i in range(N) ]
visited[0][0][0] = 1 # 낮 시작, #낮 = 홀수깊이
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
    depth = a[2]+1 #다음 경로 (다음 이동의 depth)
    s = a[3] # 벽 부순 이력 여부
    for i in range(4):
        #다음이동 위치
        xi = x+dx[i]
        yi = y+dy[i]
        if xi>=0 and xi<N and yi>=0 and yi<M:
            if table[xi][yi] == 0: #벽이 아니라면
                if xi==N-1 and yi==M-1: #끝 도착
                    print(depth)
                    exit(0)
                if min(visited[xi][yi][0:s+1]) > depth: #greedy 적용
                    #방문기록이 없었거나, 현 방문보다 경로가 길었다면
                    visited[xi][yi][s] = depth
                    que.append([xi,yi,depth,s])
            elif s < K: # 벽이고 부순 기록이 K보다 적다면
                if depth%2 == 0: #밤 -> 다음 이동이 밤이 되는 상황: 이동 가능
                    if xi==N-1 and yi==M-1: #끝 도착
                        print(depth)
                        exit(0)
                    if min(visited[xi][yi][0:s+2]) > depth:
                        visited[xi][yi][s+1] = depth
                        que.append([xi,yi,depth,s+1])
                else: #낮 -> 다음 이동이 낮이 되는 상황
                    if min(visited[xi][yi][0:s+2]) > depth+1:
                        que.append([x,y,depth,s]) # 현 위치에서 다음 탐색에 다시 보자!
#exit을 못해고 끝났다면
print(-1)
'''
#시간은 많이 줄었으나, 여전히 시간초과
#3차원배열이 아닌, 2차원 배열 + depth는 bfs 탐색의 깊이로

import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())

if N==1 and M==1:
    print(1)
    exit(0)

table = [[int(i) for i in list(input().rstrip())] for j in range(N)]
breakcount = [ [K+1 for j in range(M)] for i in range(N) ] # i,j에 도착하기까지의 벽 부순 횟수. min값을 저장한다 (greedy)
breakcount[0][0] = 0
#depth는 저장 안하나? -> 어차피 BFS로 낮은 깊이부터 탐색되므로, 깊이가 더 낮은 결과가 먼저 나옴

from collections import deque
que = deque([[0,0,1,0]])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
while que:
    a = que.popleft()
    x = a[0]
    y = a[1]
    depth = a[2]+1 #다음 경로 (다음 이동의 depth)
    s = a[3] # 벽 부순 횟수 이력 
    for i in range(4):
        #다음이동 위치
        xi = x+dx[i]
        yi = y+dy[i]
        if xi>=0 and xi<N and yi>=0 and yi<M:
            if table[xi][yi] == 0: #벽이 아니라면
                if xi==N-1 and yi==M-1: #끝 도착
                    print(depth)
                    exit(0)
                if breakcount[xi][yi] > s: #greedy 적용
                    #현 depth의 방문이 벽을 덜 부쉈다면
                    breakcount[xi][yi] = s
                        #엎어쳐도 되는 이유: 이전 이력은 이미 queue 안에 들어가 다음 탐색 진행중!
                    que.append([xi,yi,depth,s])
            elif s < K: # 벽이고 부순 기록이 K보다 적다면
                if depth%2 == 0: #밤 -> 다음 이동이 밤이 되는 상황: 이동 가능
                    if xi==N-1 and yi==M-1: #끝 도착
                        print(depth)
                        exit(0)
                    if breakcount[xi][yi] > s+1: # greedy 적용
                        breakcount[xi][yi] = s+1
                        que.append([xi,yi,depth,s+1])
                else: #낮 -> 다음 이동이 낮이 되는 상황
                    if breakcount[xi][yi] > s+1:
                        que.append([x,y,depth,s]) # 현 위치에서 다음 탐색에 다시 보자!
#exit을 못해고 끝났다면
print(-1)

##pypy로 통과