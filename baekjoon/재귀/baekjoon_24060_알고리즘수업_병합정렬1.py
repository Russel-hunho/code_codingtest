#병합정렬 알고리즘:
# 파이썬 기본 내장함수인 sort 함수가 이 병합정렬 알고리즘으로 작동된다!!

# 계속 반씩 쪼개서, 원소의 개수가 1 or 2개까지만 남을때까지 쭉 간 후,
# Tree 기준 최하단 왼쪽부터, 정렬 후 부모Node로 올라가서, 남은 자식Node들 처리하면서 쭉 올라간다.

# 코드

'''import sys
input = sys.stdin.readline
N,K = map(int,input().split())
#N: 배열 A의 크기
#K: 병합정렬 중 K번째로 저장되는 값을 구하라!
A = list(map(int,input().split()))
#A: 정렬할 배열

# 저장 횟수 확인용 광역변수
n = 0
ans = -1
def counting():
    global n
    n += 1
    return 0

# 쪼개기 + 정렬된것 합치기
def merge_sort(A,p,r):
    if p < r:
        q = (p+r)//2
        return merge_sort(A,p,q) + merge_sort(A,q+1,r) + merge(A,p,q,r)
    else: # p == r.  p > r인 경우도 있나...? q setting rule 보면 없을것.
        return [A[p]]

#쪼개져있는 두 구간을 합치면서 정렬하기
def merge(A,p,q,r):
    i = p
    j = q+1
    temp = []
    # 정렬되어있는 서로 다른 두 구간을 비교하면서, 제일 작은 값들을 temp에 쭉 쌓아두기
    while i <= q and j <= r:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    # 두 구간중 q+1~r은 이미 temp에 꽉 찬 경우:
    # 남은 p~q 구간의 값들을 temp에 다 넣어준다
    if i <= q: 
        temp += A[i:q+1]
    # 반대로 두 구간중 q+1~r이 남운경우:
    elif j <= r:
        temp += A[j:r+1]
    
    #temp값 A에 저장하기
    i = p
    j = 0
    while i <= r:
        A[i] = temp[j]
        print(temp[j])
        counting()
        global n
        global ans
        if K == n:
            ans = A[i]
        i += 1
        j += 1
    return A

merge_sort(A,0,len(A)-1)
print(ans)'''

### 시간초과.. 시간줄이기
# return을 array로 하지 말고, 그냥 없애버려도 광역변수에 저장됨!

import sys
input = sys.stdin.readline
N,K = map(int,input().split())
#N: 배열 A의 크기
#K: 병합정렬 중 K번째로 저장되는 값을 구하라!
A = list(map(int,input().split()))
#A: 정렬할 배열

# 저장 횟수 확인용 광역변수
n = 0
ans = -1
def counting():
    global n
    n += 1
    return 0

# 쪼개기 + 정렬된것 합치기
def merge_sort(A,p,r):
    if p < r:
        q = (p+r)//2
        return merge_sort(A,p,q) + merge_sort(A,q+1,r) + merge(A,p,q,r)
    else: # p == r.  p > r인 경우도 있나...? q setting rule 보면 없을것.
        return 0

#쪼개져있는 두 구간을 합치면서 정렬하기
def merge(A,p,q,r):
    i = p
    j = q+1
    temp = []
    # 정렬되어있는 서로 다른 두 구간을 비교하면서, 제일 작은 값들을 temp에 쭉 쌓아두기
    while i <= q and j <= r:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    # 두 구간중 q+1~r은 이미 temp에 꽉 찬 경우:
    # 남은 p~q 구간의 값들을 temp에 다 넣어준다
    if i <= q: 
        temp += A[i:q+1]
    # 반대로 두 구간중 q+1~r이 남운경우:
    elif j <= r:
        temp += A[j:r+1]
    
    #temp값 A에 저장하기
    i = p
    j = 0
    while i <= r:
        A[i] = temp[j]
        print(temp[j])
        counting()
        global n
        global ans
        if K == n:
            ans = A[i]
        i += 1
        j += 1
    return 0

merge_sort(A,0,len(A)-1)
print(ans)