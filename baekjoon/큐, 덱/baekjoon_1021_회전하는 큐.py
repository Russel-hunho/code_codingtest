from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Mlist = list(map(int,input().split()))
Nqueue = deque(range(1,N+1))
count = 0
for i in Mlist:
    localcount = 0
    while True:
        if Nqueue[0] == i:
            Nqueue.popleft()
            count += min(localcount, N-localcount)
            N -= 1
            break
        else:
            Nqueue.rotate(1)
            localcount += 1
print(count)