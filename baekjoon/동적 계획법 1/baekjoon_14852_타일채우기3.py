'''
N = int(input())
import sys
sys.setrecursionlimit(10000001)

def tiling(N):
    D = [1,2] #0,1
    for i in range(2,N+1):
        A = D[i-2]
        for j in range(i-1):
                        A = (A + 2*D[j])%1000000007
        D.append(A)
    return D[N]

print(tiling(N))
'''

##시간초과
# -> 내부 For문에 대해서도 DP (동적 프로그래밍)을 적용하자!
    ## = 2차원 DP
    
N = int(input())
import sys
sys.setrecursionlimit(10000001)

def tiling(N):
    D = [1,2] #0,1
    B = [1,3] #누적합
    for i in range(2,N+1):
        A = (D[i-2] + 2*B[-1]) % 1000000007
        D.append(A)
        B.append( (B[-1]+A)%1000000007 )
    return D[N]

print(tiling(N))