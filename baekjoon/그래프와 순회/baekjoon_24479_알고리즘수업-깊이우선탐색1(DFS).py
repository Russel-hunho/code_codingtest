import sys
sys.setrecursionlimit(100001) # Node의 수만큼은 해야됨
input = sys.stdin.readline
N,M,R = map(int,input().split())
graph = [[] for i in range(N+1)] #0번Node부터 N번 Node까지; node는 항상 비어있음
visited = [0]*(N+1)
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,N+1):
    graph[i] = sorted(graph[i]) # 오름차순 정리

count = 0
def DFS(graph, visited, node):
    global count
    count += 1 #방문 순서
    visited[node] = count # 방문순서 기록
    for i in graph[node]:
        if visited[i] == 0: #방문 안한 Node라면
            DFS(graph, visited, i) #재귀 실행

DFS(graph, visited, R) #시작node : R
for i in range(1,N+1):
    print(visited[i])