N = int(input())
DP = [0]*(N+1) #i번째 index: i를 1로 만드는 연산 횟수, DP[1] = 0 (이미 1)

for i in range(2,N+1):
    A,B = 1E6,1E6
    if i%3 == 0:
        A = DP[i//3]+1
    if i%2 == 0:
        B = DP[i//2]+1
    C = DP[i-1]+1
    DP[i] = min(A,B,C)

print(DP[N])