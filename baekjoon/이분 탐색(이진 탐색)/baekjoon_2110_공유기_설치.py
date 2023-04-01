import sys
input = sys.stdin.readline
N,C = map(int,input().split())
xlist = []
for _ in range(N):
    xlist.append(int(input()))

xlist.sort()

start = 1
end = (max(xlist)-min(xlist)) // (C-1)

while True:
    if start > end:
        break
    mid = (start + end)//2 # 공유기 사이의 거리의 lower bound
        #mid 값이 최대가 되게 만들고 싶음!
    count = C-1
    pre_x = xlist[0] #greedy. 끝점을 포함하는 경우가 무조건 최선
    for i in range(1,N):
        if xlist[i] - pre_x >= mid:
            count -= 1
            pre_x = xlist[i]
    #공유기를 다 소진했다면
    if count <= 0:
        ans = mid
        start = mid+1
    else:
        end = mid-1
print(ans)