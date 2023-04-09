'''
import sys
from itertools import combinations as cb
input = sys.stdin.readline
N = int(input())
Nlist = [list(map(int,input().split())) for _ in range(N)]
count = 0
for num in cb(list(range(N)),3):
    x1 = Nlist[num[0]][0]
    y1 = Nlist[num[0]][1]
    x2 = Nlist[num[1]][0]
    y2 = Nlist[num[1]][1]
    x3 = Nlist[num[2]][0]
    y3 = Nlist[num[2]][1]
    r1 = (x1-x2)**2+(y1-y2)**2
    r2 = (x2-x3)**2+(y2-y3)**2
    r3 = (x3-x1)**2+(y3-y1)**2
    if r1+r2+r3-2*max(r1,r2,r3) == 0:
        count += 1
print(count)

'''
# 시간초과

import sys
from itertools import combinations as cb
input = sys.stdin.readline
N = int(input())
Nlist = [list(map(int,input().split())) for _ in range(N)]
count = 0
for i in range(N): #직각 꼭짓점
    x1 = Nlist[i][0]
    y1 = Nlist[i][1]
    for num in cb(list(set(list(range(N)))-set([i])),2):
        x2 = Nlist[num[0]][0]
        y2 = Nlist[num[0]][1]
        x3 = Nlist[num[1]][0]
        y3 = Nlist[num[1]][1]
        if (y2-y1)*(y3-y1) = -1*(x2-x1)*(x3-x1): #직각: 기울기 곱 = -1 (y2-y1)/(x2-x1) * (y3-y1)/(x3-x1) = -1 
            count += 1
print(count)