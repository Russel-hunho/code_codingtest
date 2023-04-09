x,y,c = map(float,input().split())
#이분탐색
start = 0.001
end = min(x,y)-0.001
while True:
    if start > end:
        break
    mid = round((start+end)/2,3)
    k = (1/c) - (1/(x**2-mid**2)**0.5) - (1/(y**2-mid**2)**0.5)
    if k >= 0: # mid 값이 작은 상태
        start = round(mid+0.001,3)
    else:
        end = round(mid-0.001,3)
print(mid)