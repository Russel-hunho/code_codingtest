import sys
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append( [ int(i) for i in list(input().rstrip()) ] )

count = 0
ans = []

localcount = 0
def DFS(x,y):
    global localcount
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    if graph[x][y] == 1:
        #방문 기록
        localcount += 1
        graph[x][y] = 0
        #재귀탐색
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y+1)
        DFS(x,y-1)
        return True
    else:
        return False

for i in range(N):
    for j in range(N):
        localcount = 0 #초기화
        if DFS(i,j) == True:
            count += 1
            ans.append(localcount)

print(count)
ans.sort() # 오름차순
for i in ans:
    print(i)