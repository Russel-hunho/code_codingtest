import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    primecount = 0
    state = [False]*2 + [True] * (2*n-1)
    for i in range(2,2*n+1):
        if state[i] == True:
            if i > n:
                primecount += 1
            for j in range(2*i, 2*n+1, i):
                state[j] = False
    print(primecount)