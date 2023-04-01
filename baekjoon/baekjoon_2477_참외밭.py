import sys
input = sys.stdin.readline

K = int(input())
# 반시계: [4(북)->2(서)->3(남)->1(동)->4(북)]
vertical = [] # 3,4
horizontal = [] # 1,2
all = []
for _ in range(6):
    a,b = map(int,input().split())
    if a > 2:
        vertical.append(b)
    else:
        horizontal.append(b)
    all.append(b)
max(vertical)
horimax = max(horizontal)
vertimax = max(vertical)
Area = horimax * vertimax
#두 Max값은 연달아 나온다! 6->1 일수도 있긴 함
horiindex = all.index(horimax)
vertiindex = all.index(vertimax)
if horimax == vertimax:
    horiindex += 1
if max(horiindex,vertiindex) == 5 and min(horiindex,vertiindex) == 0:
    print(K * (Area - all[2]*all[3]) )
else:
    print(K * (Area - all[ (max(horiindex,vertiindex)+2)%6 ]*all[ (max(horiindex,vertiindex)+3)%6 ] ))