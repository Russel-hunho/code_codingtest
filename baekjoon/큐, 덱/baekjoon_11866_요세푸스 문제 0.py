from collections import deque

N,K = map(int,input().split())
Ndeque = deque(range(1,N+1)) #1부터N까지
print("<",end = "")
for i in range(N):
    Ndeque.rotate(-(K-1))
    a = Ndeque.popleft()
    print(a,end="")
    if i != N-1:
        print(", ",end="")
    else:
        print(">")