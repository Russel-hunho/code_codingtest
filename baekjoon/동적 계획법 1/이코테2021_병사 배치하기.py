##https://www.youtube.com/watch?v=5Lu34WIx2Us&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 1:00:02

# 감소하는 최대 길이 부분수열 만들기

import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))

DP = [1]*N

for i in range(1,N):
    for j in range(i):
        if A[j] > A[i]:
            DP[i] = max(DP[i], DP[j]+1)
print(N-max(DP))