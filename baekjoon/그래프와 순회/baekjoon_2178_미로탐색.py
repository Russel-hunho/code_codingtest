import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
graph = []
#그래프 만들기
for _ in range(N):
    graph.append([int(i) for i in list(input().rstrip())])
#N,M까지 이동할때의 최소 깊이: BFS로 탐색하면서 결과 나오면 끝내버리자!

def BFS():
    global N,M #index [N-1][M-1]로 도착 구하기
    queue = deque([[0,0,1]])
    graph[0][0] = 0
    while queue:
        v = queue.popleft()
        i = v[0] #0~N-1
        j = v[1] #0~M-1
        depth = v[2] #1부터 시작
        #상하좌우 탐색
        if i-1 >= 0:
            if graph[i-1][j] == 1:
                graph[i-1][j] = 0 #방문처리
                queue.append([i-1,j,depth+1])
        if i+1 < N:
            if graph[i+1][j] == 1:
                #종료점이면 바로 종료
                if i+1 == N-1 and j == M-1:
                    print(depth+1) #종료점까지 인식
                    return 0
                graph[i+1][j] = 0 #방문처리
                queue.append([i+1,j,depth+1])
        if j-1 >= 0:
            if graph[i][j-1] == 1:
                graph[i][j-1] = 0 #방문처리
                queue.append([i,j-1,depth+1])
        if j+1 < M:
            if graph[i][j+1] == 1:
                #종료점이면 바로 종료
                if i == N-1 and j+1 == M-1:
                    print(depth+1) #종료점까지 인식
                    return 0
                graph[i][j+1] = 0 #방문처리
                queue.append([i,j+1,depth+1])
BFS()