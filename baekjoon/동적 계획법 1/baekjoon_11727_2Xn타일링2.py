import sys
input = sys.stdin.readline

def tiling(n):
    F = [1,1]
    for i in range(2,n+1):
        F.append((F[-1]+2*F[-2])%10007)
    return F[n]

A = int(input())
print(tiling(A))