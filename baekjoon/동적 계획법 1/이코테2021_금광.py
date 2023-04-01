##https://www.youtube.com/watch?v=5Lu34WIx2Us&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 52:39

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    nmlist = list(map(int,input().split()))
    DP = [[0]*m for i in range(n)]
    #초기값 setting
    for i in range(n):
        DP[i][0] = nmlist[i]
    # DP 알고리즘 적용
    for i in range(1,m):
        for j in range(n):
            #left_up: 왼위에서 오는 경우
            if j == 0:
                left_up = 0
            else:
                left_up = DP[j-1][i-1]
            #left: 왼쪽에서 오는 경우
            left = DP[j][i-1]
            #left_down: 왼쪽아래에서 오는 경우
            if j == n-1:
                left_down = 0
            else:
                left_down = DP[j+1][i-1]
            #결과 update
            DP[j][i] = nmlist[j+n*i] + max(left_up,left,left_down)
    # 답 구하기
    result = 0
    for i in range(n):
        result = max(result, DP[i][m-1])
    print(result)
    print(DP)