## 핵심은, 시작시간이 아닌 끝나는 시간!!

'''
import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

A.sort(key = lambda x : (x[1],-x[0]))
    # 종료시간 기준으로 우선정렬
        # 시작시간 기준으로 내림차순 정렬
M = A[-1][1] # 마지막 종료시간

endtimelist = [A[0][1]]
starttimelist = [A[0][0]]
for i in range(1,N):
    if A[i][1] != A[i-1][1]: # endtime이 다르면
        endtimelist.append(A[i][1])
        starttimelist.append(A[i][0])

DP = [0]*(M+1)
last = 0
for i in range(1,M+1):
    if i in endtimelist:
        j = endtimelist.index(i)
        k = starttimelist[j]
        DP[i] = 1 + max(DP[0:k+1])
print(max(DP))
'''
#시간초과

'''
import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

A.sort(key = lambda x : (x[1]))
    # 종료시간 기준으로 정렬
M = A[-1][1] # 마지막 종료시간

endtimelist = [A[0][1]]
starttimelist = [A[0][0]]
for i in range(1,N):
    if A[i][1] != A[i-1][1]: # endtime이 다르면
        endtimelist.append(A[i][1])
        starttimelist.append(A[i][0])
    else:
        starttimelist[-1] = max(starttimelist[-1],A[i][0])
print(endtimelist)
print(starttimelist)

DP = [0]*(M+1)
last = 0
for i in endtimelist:
    j = endtimelist.index(i)
    k = starttimelist[j]
    DP[i] = 1 + max(DP[0:k+1])
print(max(DP))
'''

#여전히 시간초과
'''
import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

A.sort(key = lambda x : (x[1]))
    # 종료시간 기준으로 정렬
M = A[-1][1] # 마지막 종료시간

endtimelist = [A[0][1]]
starttimelist = [A[0][0]]
newA = { A[0][1]:A[0][0] }

for i in range(N):
    if A[i][1] != A[i-1][1]: # endtime이 다르면
        newA[A[i][1]] = A[i][0]
    else:
        newA[A[i][1]] = max(newA[A[i][1]],A[i][0])
print(newA)

DP = [0]*(M+1)
for i in newA.keys():
    DP[i] = 1+max(DP[0:newA[i]+1])
print(max(DP))
'''

## 20%에서 시간초과. 결국 sort 자체를 하면 안되는듯
'''
import sys
input = sys.stdin.readline

N = int(input())
A = []
M = -1
count = 0
for _ in range(N):
    B = list(map(int,input().split()))
    if B[0]==B[1]:
        count += 1
    else:
        A.append(B)
        M = max(M,B[1])

newA = dict( )
for i in range(1,M+1):
    newA[i] = -1

for a in A:
        newA[a[1]] = max(newA[a[1]],a[0])  #start time 더 큰 값으로 갱신
print(newA)

DP = [0]*(M+1)
for i in range(1,M+1):
    if newA[i] != -1:
        DP[i] = 1+max(DP[0:newA[i]+1])
print(max(DP)+count)
'''
## 또 20%에서 시간초과. DP가 문제인건가..?
# DP 아니어도 최적해다!!!!
    # endtime으로 정렬했음에서 오는 특징.
import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

A.sort(key = lambda x:(x[1],x[0]))
    #endtime으로 정렬
    #starttime으로도 정렬 for 시작하자마자 끝나는 회의
count = 0
endtime = 0
for i in range(N):
    if A[i][0] >= endtime:
        endtime = A[i][1]
        count += 1
print(count)