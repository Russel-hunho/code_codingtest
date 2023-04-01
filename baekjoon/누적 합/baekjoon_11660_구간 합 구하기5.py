'''import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = []
for _ in range(N):
    temp = list(map(int,input().split()))
    sumlist = [temp[0]]
    for i in range(1,N):
        sumlist.append(sumlist[i-1]+temp[i])
    A.append(sumlist)

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    summa = 0
    for j in range(y1-1,y2):
        if x1 == 1:
            summa += A[j][x2-1]
        else:
            summa += A[j][x2-1]-A[j][x1-2]
    print(summa)
'''
#시간초과
##-> 누적합의 누적합을 사용해 줄이자.

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = []
for j in range(N):
    temp = list(map(int,input().split()))
    sumlist = [temp[0]]
    for i in range(1,N):
        sumlist.append(sumlist[i-1]+temp[i])
    if j == 0:
        A.append(sumlist)
    else:
        A.append([]) #A[j]의 초기값 생성
        for k in range(N):
            A[j].append( A[j-1][k] + sumlist[k] )

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == 1 and y1 == 1:
        print(A[x2-1][y2-1])
    elif y1 == 1:
        print( A[x2-1][y2-1] - A[x1-2][y2-1] )
    elif x1 == 1:
        print( A[x2-1][y2-1] - A[x2-1][y1-2] )
    else:
        print( A[x2-1][y2-1] - A[x2-1][y1-2] - A[x1-2][y2-1] + A[x1-2][y1-2] )
