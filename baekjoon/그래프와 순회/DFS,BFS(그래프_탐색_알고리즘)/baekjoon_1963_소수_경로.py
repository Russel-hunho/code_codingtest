import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
primenum = [False]*2+[True]*9999 # 0부터10000까지, True만 소수
for i in range(2,10001):
    if primenum[i] == True:
        for j in range(2*i,10001,i):
            primenum[j] = False
def solve(a,b):
    if a == b:
        print(0)
        return 0
    visited = [False]*10001
    global primenum
    que = deque([[a,0]])
    visited[a] = True # 방문
    while que:
        c = que.popleft()
        x = c[0]
        depth = c[1]
        xlist = [int(i) for i in list(str(x))]
        nextx = []
        for j in list(set([i for i in range(1,10)])-{xlist[0]}):
            nextx.append(j*1000+x%1000)
        for j in list(set([i for i in range(10)])-{xlist[1]}):
            nextx.append(j*100+xlist[0]*1000+x%100)
        for j in list(set([i for i in range(10)])-{xlist[2]}):
            nextx.append(j*10+xlist[0]*1000+xlist[1]*100+xlist[3])
        for j in list(set([i for i in range(10)])-{xlist[3]}):
            nextx.append(j+(x//10)*10)
        
        for xi in nextx:
            if xi == b:
                print(depth+1)
                return 0
            if visited[xi] == False and primenum[xi] == True:
                que.append([xi,depth+1])
    #b까지 도달 실패시
    print("Impossible")
    return 0

for _ in range(T):
    a,b = map(int,input().split())
    solve(a,b)