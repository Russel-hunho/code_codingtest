import sys
x1,y1,x2,y2,x3,y3,x4,y4 = map(int,sys.stdin.readline().split())
a2 = abs((x2-x1)*(y2-y3)-(x2-x3)*(y2-y1)) / 2
a4 = abs((x4-x1)*(y4-y3)-(x4-x3)*(y4-y1)) / 2
a3 = abs((x3-x2)*(y3-y4)-(x3-x4)*(y3-y2)) / 2
a1 = abs((x1-x2)*(y1-y4)-(x1-x4)*(y1-y2)) / 2
Area = a4 + a2
Alist = [a1,a2,a1/2,a2/2,a3/2,a4/2,a1/4,a2/4,a3/4,a4/4,a1/2+(Area-(a2/2+a1/2))/2,a2/2+(Area-(a3/2+a2/2))/2]
x = Area
for a in Alist:
    if abs(Area/2-a) < x:
        ans = a
        x = abs(Area/2-a)
for i in sorted([ans,Area-ans]):
    print(i, end=" ")