import sys
input = sys.stdin.readline
N = int(input())
Slist = list(map(str,input().split()))

x,y = 1,1
movetypes =  ["L","R","U","D"]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
for s in Slist:
    for i in range(4):
        if s == movetypes[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx not in [0,N+1]:
        x = nx
    if ny not in [0,N+1]:
        y = ny
    print(x,y)
print(x,y)