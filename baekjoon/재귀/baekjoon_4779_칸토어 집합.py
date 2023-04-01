import sys
input = sys.stdin.readline

def F(n):
    if n == 0:
        return ["-"]
    else:
        return F(n-1) + [" "]*len(F(n-1)) + F(n-1)

while True:
    N = input()
    if not N:
        break
    N = int(N)
    A = F(N)
    for i in A:
        print(i,end="")
    print("")