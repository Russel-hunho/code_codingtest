import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
Adeq = deque()
for _ in range(N):
    A = int(input())
    if A <= K:
        Adeq.appendleft(A)
count = 0
i = 0
while True:
    if K == 0:
        print(count)
        break
    count += K//Adeq[i]
    K = K%Adeq[i]
    i += 1