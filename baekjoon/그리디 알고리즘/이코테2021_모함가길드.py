##https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 23:55

import sys
input = sys.stdin.readline

N = int(input())
nlist = list(map(int,input().split()))

nlist.sort()
count = 0
templen = 0
for i in range(N):
    templen += 1 #temp에 작은 값부터 추가
    if nlist[i] <= templen:
        count += 1
        templen = 0
print(count)
