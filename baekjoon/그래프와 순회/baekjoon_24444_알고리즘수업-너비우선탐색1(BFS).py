import sys
from collections import deque
input = sys.stdin.readline
N,M,R = map(int,input().split())
graph = [[] for i in range(N+1)] #0부터N까지
visited = [0]*(N+1)
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,N+1):
    graph[i] = sorted(graph[i]) # 오름차순

def BFS(graph, visited, start):
    queue = deque([start])
    count = 1
    visited[start] = count
    while queue:
        v = queue.popleft()
        for iv in graph[v]:
            if visited[iv] == 0:
                count += 1
                visited[iv] = count
                queue.append(iv)

BFS(graph, visited, R)
for i in range(1,N+1):
    print(visited[i])