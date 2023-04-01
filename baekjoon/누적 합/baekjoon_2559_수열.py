import sys
input = sys.stdin.readline
N, K = map(int,input().split())
templist = list(map(int,input().split()))

ktemp = sum(templist[0:K])
maxitemp = ktemp
    #초기값 setting 완료
for i in range(N-K):
    ktemp = ktemp + templist[i+K]-templist[i]
    maxitemp = max( ktemp, maxitemp )
print(maxitemp)