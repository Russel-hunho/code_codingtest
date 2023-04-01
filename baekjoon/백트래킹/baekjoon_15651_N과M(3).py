# 백트래킹이란? 

N,M = map(int,input().split())
A = [[i] for i in range(1,N+1)]
B = [[i] for i in range(1,N+1)]

def f(C,i):
    if i == 1:
        return C
    temp = []
    for j in C:
        for k in A:
            temp.append(j+k)
    C = temp
    return f(C,i-1)

K = f(B,M)
for x in K:
    for i in x:
        print(i, end = " ")
    print()