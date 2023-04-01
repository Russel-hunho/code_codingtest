'''import sys
N = int(sys.stdin.readline())
A = []
for i in range(N):
    A.append(sys.stdin.readline().rstrip())
A.sort(key = len)
for i in A:
    print(i)'''

import sys
N = int(sys.stdin.readline())
A = {} # "길이": [문자열들]
for i in range(N):
    k = sys.stdin.readline().rstrip()
    if len(k) in A.keys():
        if k not in A[len(k)]:
            A[len(k)].append(k)
    else:
        A[len(k)] = [k]

#key 값으로 오름차순 정렬
B = dict(sorted(A.items()))
# B = dict(sorted(A.items(),key = lambda x:x[0], reverse = True))
# print(B)
for i in B.values():
    i.sort()
    for j in i:
        print(j)