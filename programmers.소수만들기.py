def solution(nums):
    answer = 0
    l = len(nums)
    sum_arr = []
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                sum_arr.append(nums[i]+nums[j]+nums[k])
    m = max(sum_arr)
    x = list(range(2,m+1)) #소수들의 집합
    a = 0
    while True:
        b = x[a]
        x = list(set(x) - set(range(2*b,m+1,b)))
        x.sort()
        a += 1
        if a == len(x):
            break
    A = [j for j in sum_arr if j in x]
    return len(sum_arr) - len(set(sum_arr) - set(x))



###
def solution(nums):
    from itertools import combinations as cb
    sum_arr = []
    for a in cb(nums,3):
        sum_arr.append(sum(a))
    
    m = max(sum_arr)
    x = list(range(2,m+1)) #소수들의 집합
    a = 0
    while True:
        b = x[a]
        x = list(set(x) - set(range(2*b,m+1,b)))
        x.sort()
        a += 1
        if a == len(x):
            break
    A = [y for y in sum_arr if y in x]
    return len(A)