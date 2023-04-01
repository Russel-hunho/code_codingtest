# 방문을 표기한다면 중복을 줄일 수 있다!
# 일단 없이 해보자
'''
from collections import deque
N,K = map(int,input().split())

def BFS(N,K):
    time = 0
    queue = deque([[N,time]])
    while queue:
        v = queue.popleft()
        X = v[0]
        time = v[1]
        time += 1
        if K in [X-1, X+1, 2*X]:
            print(time)
            return 0
        queue.append([X-1,time])
        queue.append([X+1,time])
        queue.append([2*X,time])

if N == K:
    print(0)
else:
    BFS(N,K)
'''

# 메모리초과


from collections import deque
N,K = map(int,input().split())
visited = [0]*100001
def BFS(N,K):
    time = 0
    queue = deque([[N,time]])
    visited[N] = 1
    while queue:
        v = queue.popleft()
        X = v[0]
        time = v[1]
        time += 1
        if K in [X-1, X+1, 2*X]:
            print(time)
            return 0
        if X > 0:
            if visited[X-1] == 0:
                visited[X-1] = 1
                queue.append([X-1,time])
        if X < 100000:
            if visited[X+1] == 0:
                visited[X+1] = 1
                queue.append([X+1,time])
        if X <= 50000:
            if visited[X*2] == 0:
                visited[X*2] = 1
                queue.append([X*2,time])
if N == K:
    print(0)
else:
    BFS(N,K)