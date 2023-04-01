'''
import sys
N = int(input())
sys.setmemorylimit(10000000)
# 피보나치
def pivonacci(N):
    F = [0, 0, 1]
    for j in range(3,N+1):
        F.append(F[-1]+F[-2])
    return F[N]
print(pivonacci(N)%15746)
'''

#메모리 초과..!
# 함수내에, 수열로 계속 할당을 늘리지 말고, 피보나치에 필요한 두 수만 남기자!

'''
N = int(input())
# 피보나치
def pivonacci(N):
    a,b = 1,1
    for j in range(3,N+1):
        a,b = b,(a+b)
    return b
print(pivonacci(N+1)%15746)
'''

#시간초과 -> 값이 너무 커져서, 덧셈도 오래걸린다!

N = int(input())
# 피보나치
def pivonacci(N):
    a,b = 1,1
    for j in range(3,N+1):
        a,b = b,(a+b)%15746 #바로바로 나눠주면서, 크기를 줄여 시간 단축
    return b
print(pivonacci(N+1))