## https://www.youtube.com/watch?v=7C9RgOcvkvo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 42:51

# 붙어있는 0끼리 하나로 취급

#입력 예시
'''
4 5
00110
00011
11111
00000
'''
#출력 예시
'''
3
'''

#핵심: 현재 input을, graph형식으로 바꿔, 몇개의 단독 graph가 생성되는지를 본다!

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append( [ int(i) for i in list(input().rstrip()) ] )

print(graph)

def dfs(x,y):
    # 주어진 index를 벗어나면 그냥 False 반환
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재 Node를 방문하지 않았다면, DFS 탐색 후에, 최종은 True 반환
    if graph[x][y] == 0:
        graph[x][y] = 1 #방문처리
        # 상하좌우 연결 Node 탐색
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)        
        return True
    else: # 시작 Node를 방문한적이 있다면, 바로 False 반환
        return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1 #그래프 시작 count
print(result)