import sys
input = sys.stdin.readline

T = int(input())

def trigonal(N):
    D = [0,1,1,1,2,2,3,4,5,7]
    if N <= 9:
        return D[N]
    else:
        for i in range(10,N+1):
            D.append(D[-1]+D[-5])
        return D[N]

for _ in range(T):
    N = int(input())
    print(trigonal(N))