# 숫자가 10000보다 작거나 같은 자연수
# -> couning 정렬을 이용하자!
# 1~10000까지의 숫자의 counting을 미리 만들어놓고, 입력받은 수의 counting 값을 1씩 올리는것

import sys
N = int(sys.stdin.readline())
countinglist = [0]*10000
print(len(countinglist))
for _ in range(N):
    countinglist[ int(sys.stdin.readline())-1 ] += 1
A = N
for i in range(10000):
    k = countinglist[i]
    for _ in range(k):
        print(i+1)