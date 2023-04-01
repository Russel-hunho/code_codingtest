import sys
from collections import deque
#sys.setrecursionlimit(1001)
input = sys.stdin.readline

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited_DFS = [False]*(N+1)
visited_BFS = [False]*(N+1)
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,N+1):
    graph[i] = sorted(graph[i]) #오름차순 방문

def DFS(graph, visited, v):
    if visited[v] == False: #방문 안했다면
        #방문표시
        print(v, end=" ")
        visited[v] = True 
        for i in graph[v]: #연결 Node들에 대하여
            DFS(graph, visited, i) #재귀실행
    
def BFS(graph, visited, start):
    queue = deque([start])
    print(start, end=" ")
    visited[start] = True
    while queue:
        v = queue.popleft()
        for iv in graph[v]:
            if visited[iv] == False:
                visited[iv] = True
                print(iv, end=" ")
                queue.append(iv)
    
DFS(graph, visited_DFS, V)
print()
BFS(graph, visited_BFS, V)