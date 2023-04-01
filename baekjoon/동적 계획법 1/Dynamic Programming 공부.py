## https://www.youtube.com/watch?v=FmXZG7D8nS4&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=21&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98

# 동적 계획법이란:
# 하나의 문제를 단 한 번만 풀도록 하는 알고리즘
# 같은 문제를 단 한번만 풀게 만드는 것!

#반대개념: "분할정복"
# ex) 재귀함수를 통한 피보나치 수열


# 필수 조건 2가지
#1. 큰 문제를 작은 문제로 나눌 수 있다.
#2. 작은 문제에서 구한 정답은, 큰 문제 내에서도 동일하다.

import sys
input = sys.stdin.readline

def tiling(n):
    F = [0,1,3]
    for i in range(3,n+1):
        F.append(F[-1]+2*F[-2])
    return F[n]

while True:
    A = input()
    if not A:
        break
    A = int(A)
    print(tiling(A))