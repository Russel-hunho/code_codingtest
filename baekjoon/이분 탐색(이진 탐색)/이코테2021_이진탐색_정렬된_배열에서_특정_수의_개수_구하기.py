##https://www.youtube.com/watch?v=94RC-DsGMLo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=5&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
#23:00

# inpupt
'''
7 2
1 1 2 2 2 2 3
'''
#ouput
'''
4
'''

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
N,x = map(int,input().split())
Nlist = list(map(int,input().split()))
    #오름차순으로 이미 정렬되어 있음
    #x가 등장하는 횟수는?
print(bisect_right(Nlist,x) - bisect_left(Nlist,x))
