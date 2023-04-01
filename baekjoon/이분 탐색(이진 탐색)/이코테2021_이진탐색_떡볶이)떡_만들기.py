##https://www.youtube.com/watch?v=94RC-DsGMLo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=5&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
#12:34

# 파라메트릭 서치 이용

#input
'''
4 6 
19 15 10 17
'''
#output
'''
15
'''

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Nlist = list(map(int,input().split()))

start = 0
end = max(Nlist)

while True:
    if start >= end:
        break
    mid = (start+end)//2
    sumlen = 0
    for i in Nlist:
        if i > mid:
            sumlen += i - mid
    if sumlen >= M:
        start = mid + 1
        H = mid # 결과 저장
    else:
        end = mid - 1 #가능하지 않은 경우는 버리기

print(H)