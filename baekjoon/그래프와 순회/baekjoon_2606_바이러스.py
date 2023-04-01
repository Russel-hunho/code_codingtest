import sys
from collections import deque

N = int(input())
M = int(input())
graph = [[] for i in range(N+1)] #0~N
visited = [0]*(N+1)
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
def BFS(graph, visited, start):
    queue = deque([start])
    visited[start] = 1
    global count
    while queue:
        v = queue.popleft()
        for iv in graph[v]:
            if visited[iv] == 0:
                count += 1 #총 방문한 수 +1
                visited[iv] = 1 #방문표시
                queue.append(iv)
BFS(graph, visited, 1)
print(count)