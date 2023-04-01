'''import sys
input = sys.stdin.readline
K = 500000
state = [False]*2 + [True]*(K-1)
primes = []
for i in range(2,K+1):
    if state[i] == True:
        if i != 2:
            primes.append(i)
        for j in range(2*i, K+1, i):
            state[j] = False
T = int(input())
for _ in range(T):
    N = int(input())
    if N in [4,6]:
        print(1)
    else:
        count = 0
        for i in range(3,N//2+1):
            if i in primes and N-i in primes:
                count += 1
        print(count)'''

## 시간초과.. 각각에서 하는게 맞나..?

'''import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if N in [4,6]:
        print(1)
    else:
        count = 0
        state = [False]*2 + [True]*(N-1)
        for i in range(2,N+1):
            if state[i] == True:
                for j in range(2*i, N+1, i):
                    state[j] = False
                if i >= N//2:
                    if state[N-i] == True:
                        count += 1
        print(count)'''
        
##이것도 시간초과

import sys
input = sys.stdin.readline

T = int(input())
A = []
maxi = 0
for _ in range(T):
    temp = int(input())
    A.append(temp)
    maxi = max(maxi,temp)


state = [False]*2 + [True]*(maxi-1)
primes = []
for i in range(2,maxi+1):
    if state[i] == True:
        if i != 2:
            primes.append(i)
        for j in range(2*i, maxi+1, i):
            state[j] = False

for i in A:
    if i in [4,6]:
        print(1)
    else:
        count = 0
        j = 0
        while True:
            if state[i - primes[j]] == True:
                count += 1
            j += 1
            if primes[j] > i//2:
                break
        print(count)