import sys
from collections import deque
from itertools import combinations as cb
input = sys.stdin.readline
N,M = map(int,input())
table = []
virus_location = []
ans = N**2
for i in range(N):
    Nlist = list(map(int,input().split()))
    for j in range(N):
        if Nlist[j] == 2:
            virus_location.append([i,j])

            
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(table):
    global N,M,dx,dy
    for i in range(N):
        for j in range(N):
            if table[i][j] == 0:
                table[i][j] = 1

virus_brute = list(cb(virus_location,M))







#for virus 