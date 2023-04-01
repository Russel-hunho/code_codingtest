import sys
import math
x1,y1,r1,x2,y2,r2 = map(float,sys.stdin.readline().split())
# h = r1 sin(the1) = r2 sin(the2)
# r3 = r1 cos(the1) + r2 cos(the2)
r3sq = ((x2-x1)**2+(y2-y1)**2)
r3 = r3sq**0.5
if r3 >= r1+r2:
    print("0.000")
elif (r1+r3-r2)*(r2+r3-r1) <= 0:
    if r2 >= r1+r3:
        print( round(math.pi*(r1**2),3) )
    else:
        print( round(math.pi*(r2**2),3) )
else:
    the1 = math.acos( ( r3**2 + r1**2 - r2**2 )/(2*r3*r1) )
    the2 = math.acos( ( r3**2 + r2**2 - r1**2 )/(2*r3*r2) )
    ans = (r1**2)*the1 + (r2**2)*the2 - r3*r1*math.sin(the1)
    print(round(ans,3))