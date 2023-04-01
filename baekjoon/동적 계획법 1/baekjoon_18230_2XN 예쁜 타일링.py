import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

k = 0
def tiling(N,A,B):
    global k
    if N == 0:
        return 0
    elif N == 1:
        k += A[0]
        return 0
    elif N == 2:
        k += max(A)
    elif len(B) == 0:
        k += sum(A[0:N])
        return 0
    elif len(A) == 1:
        if N%2 == 1:
            k += A[0]
            k += sum(B[0:N//2])
        else:
            k += sum(B[0:N//2])
        return 0
    elif len(A) == 0:
        k += sum(B[0:N//2])
        return 0
    else:
        N -= 2
        if sum(A[0:2]) > B[0]:
            k += sum(A[0:2])
            A.pop(0)
            A.pop(0)
        else:
            k += B[0]
            B.pop(0)
        return tiling(N,A,B)

N,A,B = map(int,input().split())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))

Alist.sort(reverse = True)
Blist.sort(reverse = True)
print(Alist)
print(Blist)
tiling(N,Alist,Blist)
print(k)
