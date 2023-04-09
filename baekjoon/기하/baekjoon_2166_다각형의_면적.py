import sys
input = sys.stdin.readline
N = int(input())
group = []
for _ in range(N):
    x,y = map(int,input().split())
    group.append([x,y])

# 넓이 = 부분삼각형의 합: 오목이면, 오목은 알아서 빼기가 된다!
ans = 0
#기준점: 0번 점
x0 = group[0][0]
y0 = group[0][1]
for i in range(1,N-1):
    x1 = group[i][0]
    y1 = group[i][1]
    x2 = group[i+1][0]
    y2 = group[i+1][1]
    triangle = (1/2)*((x1-x0)*(y2-y0)-(x2-x0)*(y1-y0))
    #벡터의 외적 -> 오목은 음수!
    ans += triangle
print(abs(ans))