'''import sys
input = sys.stdin.readline
N = int(input())
A = [] #가로수의 집합
for _ in range(N):
    A.append(int(input()))
A.sort()
mini,maxi = A[0],A[-1]
B = [] #인접 가로수들의 간격
for i in range(N-1):
    B.append(A[i+1]-A[i])
gcd = B[0] #초기값
for i in range(N-2):
    a,b = max(gcd, B[i+1]), min(gcd,B[i+1])
    while True:
        if b == 0:
            gcd = a
            break
        a,b = b,a%b
treelist = list(range(mini,maxi+1,gcd))
print(len(treelist)-len(A))'''

##메모리초과..!
#B를 A에 덮어써서 만드는 식으로 해보자

'''import sys
input = sys.stdin.readline
N = int(input())
A = [] #가로수의 집합
for _ in range(N):
    A.append(int(input()))
A.sort()
mini,maxi = A[0],A[-1]
#인접 가로수들의 간격으로 바꾸기
for i in range(N-1):
    A[i] = A[i+1]-A[i]
gcd = A[0] #초기값
for i in range(N-2):
    a,b = max(gcd, A[i+1]), min(gcd,A[i+1])
    while True:
        if b == 0:
            gcd = a
            break
        a,b = b,a%b
treelist = list(range(mini,maxi+1,gcd))
print(len(treelist)-len(A))'''

##여전히 메모리초과
#treelist도 없애보자

import sys
input = sys.stdin.readline
N = int(input())
A = [] #가로수의 집합
for _ in range(N):
    A.append(int(input()))
A.sort()
mini,maxi = A[0],A[-1]
#인접 가로수들의 간격으로 바꾸기
for i in range(N-1):
    A[i] = A[i+1]-A[i]
gcd = A[0] #초기값
for i in range(N-2):
    a,b = max(gcd, A[i+1]), min(gcd,A[i+1])
    while True:
        if b == 0:
            gcd = a
            break
        a,b = b,a%b
L = (maxi-mini)//gcd + 1
print(L-N)