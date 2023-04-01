import sys
input = sys.stdin.readline

def tiling(n):
    F = [1,1,3]
    for i in range(3,n+1):
        F.append(F[-1]+2*F[-2])
    return F[n]

while True:
    A = input()
    if not A:
        break
    A = int(A)
    print(tiling(A))