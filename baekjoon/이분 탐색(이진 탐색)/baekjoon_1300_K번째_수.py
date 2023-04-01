'''
N = int(input())
k = int(input())
from bisect import bisect_left

A = []
for i in range(1,N+1):
    temp = []
    for j in range(1,N+1):
        temp.append(i*j)
    A.append(temp)

start = 1
end = min(10**9,N**2)
while True:
    if start > end:
        break
    mid = (start+end)//2
    lesscount = 0
    samecount = 0
    for i in range(N):
        a = bisect_left(A[i],mid)
        lesscount += a # mid보다 작은 값의 개수
        if A[i][a] == mid:
            samecount += 1
    if lesscount < k and k <= lesscount + samecount:
        ans = mid
        break
    elif lesscount >= k:
        end = mid-1
    else:
        start = mid + 1
print(ans)
'''
# 메모리 초과

N = int(input())
k = int(input())

start = 1
end = min(10**9,N**2)
while True:
    mid = (start+end)//2
    lesscount = 0
    samecount = 0
    for i in range(1,N+1): # i*1 ~ i*N
        lesscount += min((mid-1)//i,N) # mid보다 작은 값의 개수
        if mid%i == 0 and mid <= N*i: # mid가 i단에 포함되어있다면
            samecount += 1
    # 이진탐색
    if lesscount < k and k <= lesscount + samecount:
        ans = mid
        break
    elif lesscount >= k:
        end = mid - 1
    else:
        start = mid + 1
print(ans)