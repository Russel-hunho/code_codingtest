N,X = map(int,input().split())

#N 버거의 층수
DP = [1]
for i in range(N):
    DP.append(DP[-1]*2+3)

def burger(N,X): #N버거를 X개까지 먹었을 때 패티 수
    if N == 0:
        if X == 0:
            return 0
        else:
            return 1
    if X <= 1:
        return 0
    elif X <= DP[N-1]+1:
        return burger(N-1,X-1)
    else:
        return (2**N-1) + 1 + burger(N-1,X-(DP[N-1]+2))

print(burger(N,X))