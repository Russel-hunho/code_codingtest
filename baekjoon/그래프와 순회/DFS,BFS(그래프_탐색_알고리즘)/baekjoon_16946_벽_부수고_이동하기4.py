import sys
input = sys.stdin.readline
from collections import deque
N,M = map(int,input().split())
wallmap = [[int(i) for i in list(input().rstrip())] for j in range(N)]
graphdepth = [0] #그래프의 숫자에 따른 깊이 저장, index 1부터 시작
graph = [[0]*M for i in range(N)] # 서로 연결된 점들끼리 같은 숫자로 표기, 1부터 시작
graphcount = 0 #1부터 시작
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def connected(x,y):
    global N,M,dx,dy, graphcount
    global wallmap, graph, graphdepth
    if wallmap[x][y] == 1: #벽이라면
        return 0 #종료
    if graph[x][y] != 0: #이미 그래프로 반영된 점이라면
        return 0 #종료
    
    count = 1
    graphcount += 1 # K번째
    que = deque([[x,y]])
    graph[x][y] = graphcount # 첫 점 방문처리
    while que:
        a = que.popleft()
        xi = a[0]
        yi = a[1]
        for i in range(4):
            xii = xi + dx[i]
            yii = yi + dy[i]
            if xii >= 0 and xii < N and yii >= 0 and yii < M:
                if wallmap[xii][yii] != 1 and graph[xii][yii] == 0: #벽이 아니고, 방문 안한 점이라면
                    graph[xii][yii] = graphcount #방문처리
                    count += 1 #연결된 점 수 추가
                    que.append([xii,yii])
    graphdepth.append(count) #K번째 그래프의 연결점 수 추가
    return 0        

# 그래프 체크
for i in range(N):
    for j in range(M):
        connected(i,j)

# 정답 구하기
for i in range(N):
    temp = ""
    for j in range(M):
        if wallmap[i][j] == 0:
            temp += "0"
        else:
            c = 1 #연결된 점 수
            group = []
            for k in range(4):
                i2 = i+dx[k]
                j2 = j+dy[k]
                if i2 >=0 and j2>=0 and i2<N and j2<M:
                    group.append(graph[i2][j2]) #벽이면 0, 아니면 포함되어있는 graph의 수가 들어감
            for k in set(group):
                c += graphdepth[k]
            temp += str(c%10)
    print(temp)
print(graph)
print(graphdepth)
print(graphcount)