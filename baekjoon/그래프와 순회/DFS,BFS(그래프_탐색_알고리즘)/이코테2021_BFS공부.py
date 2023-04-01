## https://www.youtube.com/watch?v=7C9RgOcvkvo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 35:20
#DFS부터 공부하고 오는게 좋다.

#queue를 이용한다!
from collections import deque
    #deque로 queue 구현
    
def BFS(graph, start, visited):
    #queue 구현 + start를 넣고 시작한다.
    queue = deque([start])
    visited[start] = True
        #방문 기록
    
    while queue:    #queue가 빈 채로 끝날때까지
        #queue의 첫 노드 출력
        v = queue.popleft()
        print(v, end=" ")
        #첫 노드 v에 인접한 노드 모두 방문&queue에 넣기
        for i in graph[v]:
            if not visited[i]: #방문 안한 노드라면
                queue.append(i)
                visited[i] = True

graph = [
    [], #0번 Node
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9 #0부터8까지의 Node

BFS(graph, 1, visited) #1번 Node부터 시작