M = int(input())
N = int(input())
primes = []
numstate = [False,False]+[True]*(N-1)
for i in range(2,N+1):
    if numstate[i]:
        primes.append(i)
        for j in range(2*i,N+1,i):
            numstate[j] = False
minnum = 10000
suma = 0
print(primes)
for k in primes:
    if k >= M:
        minnum = min(minnum,k)
        suma += k

if suma == 0:
    print(-1)
else:
    print(suma)
    print(minnum)