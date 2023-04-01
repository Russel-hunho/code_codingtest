import sys
input = sys.stdin.readline
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
#외적이 양수면 반시계, 음수면 시계, 0이면 일직선
A = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
if A == 0:
    print(0)
elif A > 0:
    print(1)
else:
    print(-1)