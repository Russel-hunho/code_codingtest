##https://www.youtube.com/watch?v=5Lu34WIx2Us&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 27:30

# 우선 재귀로 풀어보기
'''
import sys
input = sys.stdin.readline

N = int(input())
K = list(map(int,input().split()))

def ant(K):
    if len(K) == 1:
        return K[0]
    elif len(K) == 2:
        return max(K)
    else:
        return max( K[0]+ant(K[2:]) , ant(K[1:]) )

print(ant(K))
'''

# DP로 바꾸기

import sys
input = sys.stdin.readline

N = int(input())
K = list(map(int,input().split()))

DP = [0]*N
def ant(K):
    if len(K) == 1:
        return K[0]
    elif len(K) == 2:
        return max(K)
    else:
        DP[0] = K[0]
        DP[1] = max(K[0:2])
        for i in range(2,N):
            DP[i] = max( (K[i]+DP[i-2]), DP[i-1] )
        return DP[N-1]

print(ant(K))