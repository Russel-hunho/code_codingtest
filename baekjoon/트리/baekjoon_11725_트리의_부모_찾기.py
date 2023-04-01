import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N+1)] #0~N
parent = [-1 for i in range(N+1)] #0~N
for i in range(N-1): # N-1개의 간선
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def BFS(graph, parent):
    parent[1] = 0 #방문처리
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if parent[u] == -1:#방문 안한 노드라면
                parent[u] = v #부모노드 저장
                queue.append(u)
#실행
BFS(graph, parent)
#출력
for i in range(2,N+1):
    print(parent[i])