F,S,G,U,D = map(int,input().split())
#F: 건물 층 (max)
#S: 현재 층
#G: target 층
#U: 위로 U층
#D: 아래로 D층
visited = [False]*(F+1)
visited[S] = True # 시작점
from collections import deque
que = deque([[S,0]])
while que:
    a = que.popleft()
    s = a[0]
    depth = a[1]
    two_s = [s+U,s-D]
    for si in two_s:
        if si > 0 and si < F+1:
            if si == G:
                print(depth+1)
                exit(0)
            if visited[si] == False:
                visited[si] = True
                que.append([si,depth+1])

print("use the stairs")