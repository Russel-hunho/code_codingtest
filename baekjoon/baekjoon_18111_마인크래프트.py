'''
import sys
input = sys.stdin.readline
N,M,B = map(int,input().split())
earth = []
for _ in range(N):
    earth.append(list(map(int,input().split())))

possible = dict()
for a in range(257):    
    inven = 0
    time = 0
    for i in range(N):
        for j in range(M):
            k = earth[i][j] - a
            if k < 0: #더 쌓아야 됨
                time += -k
                inven -= -k
            else:
                time += 2*k
                inven += k
    if inven + B >= 0:
        possible[time] = a #작은 값부터 탐색하므로, 중복되면 높은 값으로 업데이트됨
    else: #이미 인벤을 넘어갔으므로, 이 이상은 탐색할 필요 없음
        break 
A = dict(sorted(possible.items(),key = lambda x:x[0]))[0]
print(A[0],A[1])
'''

# 시간초과
import sys
input = sys.stdin.readline
N,M,B = map(int,input().split())
earth = [0]*257 #높이 0부터 256까지
for _ in range(N):
    Mlist = list(map(int,input().split()))
    for i in Mlist:
        earth[i] += 1
possible = dict()
for a in range(257):
    inven = 0
    time = 0
    for i in range(257):
        k = i-a
        if k < 0:
            time += (-k)*earth[i]
            inven -= (-k)*earth[i]
        else:
            time += 2*k*earth[i]
            inven += k*earth[i]
    if inven + B >= 0:
        print(time,a)
        possible[time] = a #작은 값부터 탐색하므로, 중복되면 높은 값으로 업데이트됨
    else: #이미 인벤을 넘어갔으므로, 이 이상은 탐색할 필요 없음
        break
print(list(sorted(possible.items(),key = lambda x:x[0])))
A = list(sorted(possible.items(),key = lambda x:x[0]))[0]
print(A[0],A[1])