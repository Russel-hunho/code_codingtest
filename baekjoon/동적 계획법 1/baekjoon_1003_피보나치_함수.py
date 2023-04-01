import sys
input = sys.stdin.readline
T = int(input())

def fibonacci(N):
    DP = [1,0]+[0]*N #총 N+2개, index: 0~N+1까지
    for i in range(2,N+2):
        DP[i] = DP[i-1]+DP[i-2]
    return [DP[N], DP[N+1]]

for _ in range(T):
    N = int(input())
    A = fibonacci(N)
    a,b = A[0], A[1]
    print("{} {}".format(a,b))
    