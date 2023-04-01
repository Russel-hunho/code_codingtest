import sys
input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N):
    A.append(list(map(str, input().split())))

A = sorted(A, key = lambda x:(int(x[0])))

for i in A:
    print("{} {}".format(int(i[0]),i[1]))
    