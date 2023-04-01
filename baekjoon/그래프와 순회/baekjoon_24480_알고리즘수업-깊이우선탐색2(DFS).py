import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline
N,M,R = map(int, input().split())
graph = [[] for i in range(N+1)] #0~N
visited = [0]*(N+1) #0~N
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
#내림차순
for i in range(1,N+1):
    graph[i] = sorted(graph[i], reverse = True)
    
count = 0
def DFS(graph, visited, node):
    global count
    count += 1
    visited[node] = count
    for inode in graph[node]:
        if visited[inode] == 0: # 방문 안했다면
            DFS(graph, visited, inode)

DFS(graph, visited, R)
for i in range(1,N+1):
    print(visited[i])