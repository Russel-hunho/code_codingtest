'''
import sys
from itertools import combinations as cb
input = sys.stdin.readline
N = int(input())
pointx = {i : [] for i in range(1,100001)} #x값이 i인 점들의 y값 모음
pointy = {i : 0 for i in range(1,100001)} #y값이 i인 점들의 수
for _ in range(N):
    x,y = map(int,input().split())
    pointx[x].append(y)
    pointy[y] += 1

count = 0
for i in range(1,100001):
    for ylist in cb(pointx[i],2): #x가 i인 점들의 y값 중 2개 선택
        count += pointy[ylist[0]]+pointy[ylist[1]]-2
print(count)

'''
import sys
from itertools import combinations as cb
input = sys.stdin.readline
N = int(input())
pointx = {i : [] for i in range(1,100001)} #x값이 i인 점들의 y값 모음
pointy = {i : 0 for i in range(1,100001)} #y값이 i인 점들의 수
for _ in range(N):
    x,y = map(int,input().split())
    pointx[x].append(y)
    pointy[y] += 1

count = 0
for i in range(1,100001):
    lx = len(pointx[i])
    for y in pointx[i]: #x가 i인 점들의 y값 중 2개 선택
        count += (pointy[y]-1)*(lx-1)
print(count)
