import sys
input = sys.stdin.readline
from collections import deque
wall_map = [[0]*8 for i in range(8)]
for i in range(8):
    iboard = list(input().rstrip())
    for j in range(8):
        if iboard[j] == "#":
            wall_map[i][j] = 1 #1이 벽
            
dx = [1,1,1,0,-1,-1,-1,0,0] #상하좌우대각선+제자리 총 9가지
dy = [-1,0,1,1,1,0,-1,-1,0]

que = deque([[7,0,0]])#왼쪽아래 출발
depth_state = 0
while que:
    a = que.popleft()
    x = a[0]
    y = a[1]
    depth = a[2]
    # 다음 깊이 탐색시 벽 내리기!
    if depth_state != depth: # depth가 바뀌면
        depth_state = depth #현 depth 반영
        for j in range(8): #맨 아랫줄 먼저 wall 다 지우기
            wall_map[7][j] = 0
        for i in range(6,-1,-1): #맨 아랫줄 빼고 아래부터 탐색
            for j in range(8):
                if wall_map[i][j] == 1:
                    wall_map[i+1][j] = 1
                    wall_map[i][j] = 0
    if wall_map[x][y] == 1:
        continue
    # 다음 탐색
    for i in range(9):
        xi = x+dx[i]
        yi = y+dy[i]
        if xi >= 0 and yi >= 0 and xi < 8 and yi < 8:
            if xi == 0 and yi == 7:
                print(1)
                exit(0)
            if wall_map[xi][yi] == 0:
                que.append([xi,yi,depth+1])
#실패시
print(0)