##https://www.youtube.com/watch?v=5Lu34WIx2Us&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 36:13

X = int(input())

DP = [0]*30000

def makeone(x):
    if x == 1:
        return 0
    for i in range(1,x):
        A,B,C = i,i,i
        if i%5 == 0:
            A = DP[i//5]+1
        if i%3 == 0:
            B = DP[i//3]+1
        if i%2 == 0:
            C = DP[i//2]+1
        D = DP[i-1]+1
        DP[i] = min(A,B,C,D)
    return DP[x-1]

print(makeone(X))