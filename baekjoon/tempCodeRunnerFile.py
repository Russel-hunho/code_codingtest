import sys
N = int(sys.stdin.readline())
A = {} # "길이": [문자열들]
for i in range(N):
    k = sys.stdin.readline().rstrip()
    if len(k) in A.keys():
        A[len(k)].append(k)
    else:
        A[len(k)] = [k]