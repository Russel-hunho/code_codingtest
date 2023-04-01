import sys
sys.setrecursionlimit(51*51)
input = sys.stdin.readline
T = int(input())

def DFS(x,y,M,N):
    if x < 0 or y < 0 or x >= M or y >= N:
        return False
    if graph[x][y] == 1:
        #방문처리
        graph[x][y] = 0
        #재귀실행
        DFS(x+1,y,M,N)
        DFS(x-1,y,M,N)
        DFS(x,y+1,M,N)
        DFS(x,y-1,M,N)
        return True
    else:
        return False

for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*N for i in range(M)]
    # table 만들기
    for _ in range(K):
        x,y = map(int,input().split())
        graph[x][y] = 1
    #graph 탐색하며 수 세기
    result = 0 #그래프의 수
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                result += 1
                DFS(i,j,M,N)
    print(result)