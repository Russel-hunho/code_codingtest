orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

from itertools import combinations
def solution(orders, course):
    answer = []
    for i in course:
        A = dict()
        for j in orders:
            i_courselist = list(map(list,combinations(j,i)))
            for k in i_courselist:
                k.sort()
                k = "".join(k)
                if k in A.keys():
                    A[k] += 1
                else:
                    A[k] = 1
        if A != dict():
            Max_count = max(A.values())
            if Max_count >= 2:
                for k in A.keys():
                    if A[k] == Max_count:
                        answer.append(k)
    answer.sort()
    return answer