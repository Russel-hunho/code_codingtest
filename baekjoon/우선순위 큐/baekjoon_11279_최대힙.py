import sys
input = sys.stdin.readline
import heapq

h = [] #힙으로 사용
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            #파이썬의 heapq는 최소힙구조이므로, 넣을때 -1을 곱해 넣고, 뺄 때 -1을 또 곱하여, 최대힙구조로 사용 가능하다!
            print( (-1)*heapq.heappop(h) )
    else:
        heapq.heappush(h,-x)