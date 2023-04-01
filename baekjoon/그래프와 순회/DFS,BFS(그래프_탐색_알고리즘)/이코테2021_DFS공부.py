##https://www.youtube.com/watch?v=7C9RgOcvkvo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 26:35

def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:  #방문 안했던 노드라면?
            dfs(graph, i, visited)  #재귀 실행 -> 자연스럽게 stack 느낌으로 된다.

# 각 노드가 연결된 정보 표현: 2차원 리스트
graph = [
    [],         #0은 존재 X
    [2,3,8],    #1은 2,3,8과 연결
    [1,7],      #2는 1,7과 연결
    [1,4,5],    #3은 1,4,5와 연결
    [3,5],      
    [3,4],
    [7],
    [2,5,8],
    [1,7]
]

#각 노드가 방문된 정보를 표현: 1차원 리스트
visited = [False]*9     #0부터 8까지. 아직 다 방문 안했으므로 다 False

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
    #1부터 시작해보겠다.
    