import sys
imput = sys.stdin.readline
N = int(input())
r1,c1,r2,c2 = map(int,input().split())

move_x = [-2,-2,0,0,2,2]
move_y = [-1,+1,-2,+2,-1,+1]

from collections import deque
visited = [ [False]*N for i in range(N) ]
visited[r1][c1] = True
que = deque([ [r1,c1,0] ])
while que:
    a = que.popleft()
    x = a[0]
    y = a[1]
    depth = a[2]
    for i in range(6):
        r = x+move_x[i]
        c = y+move_y[i]
        if r in range(N) and c in range(N):
            if r==r2 and c==c2:
                print(depth+1)
                exit(0)
            if visited[r][c] == False:
                visited[r][c] = True
                que.append([r,c,depth+1])
print(-1)