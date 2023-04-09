A,B,C = map(int,input().split())
DP = []
A = A%C
def f(a,b):
    global C
    if b == 1:
        return a
    elif b%2 == 0:
        return (f(a,b//2)**2)%C
    else:
        return (f(a,b//2)**2*a)%C
ans = f(A,B)
print(ans)