import sys
alist = list(map(int,sys.stdin.readline().split()))
from itertools import permutations as per
totalcase = list(per(alist,8))
ans = 0
for i in totalcase:
    state = 0
    for j in range(8):
        r1 = i[j]
        r2 = i[(j+1)%8]
        r3 = i[(j+2)%8]
        #45도의 특이성 이용
        if r2 < (2**0.5) * r1*r3/(r1+r3): #오목
            state = 1
            break
    if state == 0:
        ans += 1
print(ans)