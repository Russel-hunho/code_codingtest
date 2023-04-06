s,t = map(int,input().split())
from collections import deque
if s==t:
    print(0)
    exit(0)
if t==0:
    print("-")
    exit(0)
que = deque([[s,""]])
k = 0
while que:
    a = que.popleft()
    x = a[0]
    state = a[1]
    if t%(x**2) == 0 and x != 1:
        x1 = x**2
        if x1 == t:
            print(state+"*")
            exit(0)
        else:
            que.append([x1,state+"*"])
    if t%2 == 0 and (t//2)%x==0:
        x2 = x*2
        if x2 == t:
            print(state+"+")
            exit(0)
        else:
            que.append([x2,state+"+"])
    if s != 1 and k == 0: # 딱 한번만
        if t == 1:
            print("/")
            exit(0)
        que.append([1,"/"])
        k += 1


#불가능        
print(-1)