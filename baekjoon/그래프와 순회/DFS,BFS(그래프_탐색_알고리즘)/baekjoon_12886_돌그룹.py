'''
A,B,C = map(int,input().split())
from collections import deque
que = deque([[A,B,C]])
k = [[0,1,2],[0,2,1],[1,2,0]]
while que:
    a = que.popleft()
    for i in range(3):
        x = k[i][0] #비교
        y = k[i][1] #비교
        z = k[i][2] #나머지놈
        x = a[x]
        y = a[y]
        z = a[z]
        if x == y and y == z:
            print(1)
            exit(0)
        if x != y:
            x,y = min(x,y),max(x,y)
            x,y = 2*x,y-x
            que.append([x,y,z])
print(0)
'''

# 시간초과

'''
A,B,C = map(int,input().split())
from collections import deque
X = sorted([A,B,C])
A = X[0]
B = X[1]
C = X[2]
que = deque([[A,B,C]])
k = [[0,1,2],[0,2,1],[1,2,0]]
visited = [False]*((1000**2)*500)
visited[1000**2*(A-1)+1000*(B-1)+(C-1)] = True
while que:
    a = que.popleft()
    for i in range(3):
        x = a[k[i][0]] #비교
        y = a[k[i][1]] #비교
        z = a[k[i][2]] #나머지놈
        if x == y and y == z:
            print(1)
            exit(0)
        if x != y and y!=z and z!=x:
            x,y = min(x,y),max(x,y)
            x,y = 2*x,y-x
            X = sorted([x,y,z])
            x = X[0]
            y = X[1]
            z = X[2]
            if visited[1000**2*(x-1)+1000*(y-1)+(z-1)] == False:
                visited[1000**2*(x-1)+1000*(y-1)+(z-1)] = True
                que.append([x,y,z])
print(0)
'''

#메모리초과

A,B,C = map(int,input().split())
from collections import deque
X = sorted([A,B,C])
A = X[0]
B = X[1]
C = X[2]
que = deque([[A,B,C]])
k = [[0,1,2],[0,2,1],[1,2,0]]
visited = [False]*(1500**2) ## A+B+C 총합은 변하지 않음 -> A,B만 알면 C는 자동
visited[1500*(A-1)+(B-1)] = True
while que:
    a = que.popleft()
    for i in range(3):
        x = a[k[i][0]] #비교
        y = a[k[i][1]] #비교
        z = a[k[i][2]] #나머지놈
        if x == y and y == z:
            print(1)
            exit(0)
        x,y = min(x,y),max(x,y)
        x,y = 2*x,y-x
        X = sorted([x,y,z])
        x = X[0]
        y = X[1]
        z = X[2]
        if visited[1500*(x-1)+(y-1)] == False:
            visited[1500*(x-1)+(y-1)] = True
            que.append([x,y,z])
print(0)