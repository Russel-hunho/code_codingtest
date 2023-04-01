##https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 11:14
N,K = map(int,input().split())

count = 0

# 1을 빼거나
# K로 나누거나
# -> K로 나누는게 훨씬 빠를것!

while True:
    if N == 1:
        print(count)
        break
    if N%K == 0:
        count += 1
        N //= K
    else:
        a = N%K
        count += a
        N -= a